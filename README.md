# Bibliothèque d'horloges IPAudio Pro

`registry.json` est la bibliothèque embarquée, utilisable sans Internet. Les coordonnées sont normalisées sur une image 16:9. Un championnat peut avoir plusieurs habillages selon le diffuseur. Les coupes peuvent avoir des habillages différents.

Un profil observé ne signifie pas que toutes les retransmissions de cette compétition sont prises en charge. `fixture_needed` désigne une compétition pour laquelle aucune géométrie spécifique n'est encore validée. La recherche automatique reste disponible.

Ajouter une variante : relever uniquement la zone de l'horloge et du temps additionnel, vérifier plusieurs minutes différentes et un passage de minute, puis obtenir cinq lectures cohérentes sur le récepteur. Ajouter le format à la compétition correspondante seulement après cette vérification. Ne jamais ajouter de compte IPTV, URL de flux ou référence privée.

Les régions apprises sur le Vu+ restent dans `/etc/enigma2/ipaudio-pro-scoreboard-layouts.json`. Elles sont prioritaires. Un échec sur une région connue déclenche la recherche des autres profils dans le même budget OCR ; le réseau n'est jamais requis pendant une synchronisation.

Précision : l'horloge affichée est entière. Les décalages en millisecondes sont des estimations rattachées aux PTS ; l'intervalle d'incertitude et la dispersion des cinq lectures doivent accompagner le contrôle. Une valeur affichée à la milliseconde n'établit pas une précision de 1 ms.

Ce dossier est prêt à être versionné dans le dépôt IPAudio Pro. Aucune publication ou mise à jour automatique depuis GitHub n'est activée sans dépôt identifié.

