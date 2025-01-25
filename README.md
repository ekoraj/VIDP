
################Comment demarrer VIDP
#docker-compose build #construire les containers
#docker-compose up # démarrer les containers
#######################################
VideoP: Pipeline Hybride de Traitement Vidéo
Description du Projet
VideoP est un pipeline automatisé de traitement vidéo qui traite les médias localement, génère des métadonnées, et centralise les résultats dans le cloud.
Architecture et Composants
Pipeline Local (Pods)

Downscale Pod: Compression et redimensionnement des vidéos
LangIdent Pod: Détection de la langue parlée
Subtitle Pod: Génération automatique des sous-titres
Animal Detect Pod: Identification des animaux dans les vidéos

Infrastructure Cloud

Traitement sur instances EC2
Équilibrage de charge
Stockage:

Résultats dans Amazon S3
Métadonnées dans DynamoDB



Interface Utilisateur

Page web hébergée sur Apache2
Visualisation des vidéos et métadonnées

Résultats
Livrables

Vidéos compressées
Métadonnées (langue, sous-titres, animaux)
Vidéos originales
Interface web de consultation

Objectifs

Centralisation sécurisée des données
Accessibilité et exploration facile des contenus
######################
Le projet peut sous titrer correctement les videos en francais!!!!

