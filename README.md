# data extraction
FR/Ce programme est un programme python qui permet d'exctraire les données d'un excel et les mettres sur une base de donnée MYSQL, MariaDB et InfluxDB
Pour ce faire, il faut les librairies pandas, mysql-connector-python, os, openpyxlsx et influxdb

# Initialisation
Il vous faut un IDE (par exemple PyCharm) pour lancer le programme (assurer-vous d'avoir tous installés).
Lors du démarage du programme, le programme va vous demandez plusieurs chose:

Extraction: Il permet de convertir des fichiers xlsx en csv ou de prendre les fichier csv et de les exporter vers une base de donnée

Connexion: Il permet de se connecter sur une base de donnée supporter par le programme (MySQL, MariaDB et InfluxDB)
# Extraction
Lorsque vous choisisez l'option extraction il vous proposera plusieurs option:
Si on veux prendre un fichier plus recent, le programme vous demmandera le chemin du fichier sinon vous pouvez prendre un document spécifique, par contre il faudra renseigner le chemin et le nom du fichier.

![image](https://github.com/lgutel/data-extraction/assets/150175199/a7e1e842-1ce0-4a7c-8515-c5386be5ffaa)

Puis le programme convertira le fichier le plus recent ou pas en cvs dans le dossier C:\doc_csv\, et vous avez justes à choisir et à confirmé votre choix
![image](https://github.com/lgutel/data-extraction/assets/150175199/cb8ee835-3d9d-4400-92a3-f7229c7a54a3)

Il vous demandera de selectionner un type de BDD et vous demmendera votre couple de login/mot de passe avec le nom de la base de donnée

![image](https://github.com/lgutel/data-extraction/assets/150175199/dae54155-177b-4824-b90f-b1889236e971)

L'option manuel propose de lire, écrire et d'ajout des tables. Pour ajouter des donnée dans une tables ou pour créer une tables, il faut connaitre les attribue SQL (VARCHAR, DATE etc...)
fonction lecteur: 

![image](https://github.com/lgutel/data-extraction/assets/150175199/2cf17a5f-08bd-4c2b-9465-c0f4378acda0)

fonction ajout de table:

![image](https://github.com/lgutel/data-extraction/assets/150175199/bd747c77-9b6f-452d-ae18-71e7e915376b)

fonction ajout de donnée:

![image](https://github.com/lgutel/data-extraction/assets/150175199/2ccfb0a4-ed3c-4513-9ae8-22596f4c207e)

Et l'option automatique vous propose import du document que vous avez exporté lors de la convetion du document. Et si vous n'avez qu'un fichier csv c'est pas grave car le programme peux l'exporter 

![image](https://github.com/lgutel/data-extraction/assets/150175199/85bc0af7-82f6-4da3-92e2-66ab5950b90c)

# Connexion
Lorsque vous choisisez l'option connexion, il faudra renseigner le type de BDD votre couple de login/mot de passe avec le nom de la base de donnée
Vous pouvez accéder qu'au mode manuel car vous n'avez pas exporter de fichier 

![image](https://github.com/lgutel/data-extraction/assets/150175199/88f3eea3-319e-43f6-a052-3531709404a7)

