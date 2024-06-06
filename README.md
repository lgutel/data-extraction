# data extraction
FR/Ce programme est un programme python qui permet d'exctraire les données d'un excel et les mettres sur une base de donnée MYSQL, MariaDB et InfluxDB
Pour ce faire, il faut les librairies pandas, mysql-connector-python, os et influxdb

# Initialisation
Il vous faut un IDE (par exemple PyCharm) pour lancer le programme (assurer-vous d'avoir tous installé).
Lors du démmarage du programme, le programme va vous demandez plusieurs chose:

Extraction: Il permet de convertir des fichiers xlsx en csv ou de prendre les fichier csv et de les exporter vers un base de donnée

Connexion: Il permet de se connecter sur une base de donnée supporter par le programme (MySQL, MariaDB et InfluxDB)

Lorsque vous choisisez l'option extraction il vous proposera plusieurs option:
-Si on veux prendre un fichier plus recent, le programme vous demmandera le chemin du fichier ![image](https://github.com/lgutel/data-extraction/assets/150175199/a7e1e842-1ce0-4a7c-8515-c5386be5ffaa)
Puis le convertira en cvs dans le dossier C:\doc_csv\, et vous avez justes à choisir et à confirmé votre choix
![image](https://github.com/lgutel/data-extraction/assets/150175199/cb8ee835-3d9d-4400-92a3-f7229c7a54a3)
