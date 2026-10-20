"""Validate public clock geometry without IPTV accounts, images or dependencies."""
import json
import math
import re
from pathlib import Path


def check(data):
    if data.get('schema_version')!=1:raise ValueError('unsupported_schema')
    formats=data.get('formats')
    if not isinstance(formats,dict) or not 1<=len(formats)<=128:raise ValueError('invalid_formats')
    for name,row in formats.items():
        if not re.fullmatch('[a-z0-9_]{1,40}',name):raise ValueError('invalid_id')
        for field in ('clock','extra'):
            if field=='extra' and field not in row:continue
            box=row.get(field)
            if not isinstance(box,list) or len(box)!=4:raise ValueError('invalid_box')
            if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and 0<=v<=1 for v in box):raise ValueError('invalid_coordinate')
            if not box[0]<box[2] or not box[1]<box[3]:raise ValueError('reversed_box')
        if not row.get('evidence'):raise ValueError('missing_evidence')
    for league,row in data.get('competitions',{}).items():
        if any(name not in formats for name in row['formats']):raise ValueError('unknown_format')
        if not row.get('coverage'):raise ValueError('missing_coverage')
    return len(formats)


if __name__=='__main__':
    path=Path(__file__).resolve().parents[1]/'IPAudioPro/scoreboards/registry.json'
    count=check(json.loads(path.read_text(encoding='utf-8')))
    for bad in ([0,0,2,1],[1,0,0,1],[False,0,1,1],[0,0,float('nan'),1]):
        try:check({'schema_version':1,'formats':{'test':{'clock':bad,'evidence':'test'}}})
        except ValueError:continue
        raise RuntimeError('invalid_geometry_accepted')
    print('Validated',count,'clock formats; invalid coordinate tests passed.')

