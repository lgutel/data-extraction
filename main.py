import os
import pandas as pd
from SQL import connexionMySQL_MariaDB, connexionInfluxDB

def fichierleplusrecent(chemin):
    fichiers_excel = [fichier for fichier in os.listdir(chemin) if fichier.lower().endswith(".xlsx")]

    if not fichiers_excel:
        print("Aucun fichier Excel trouvé dans le répertoire spécifié.")
    else:
        fichiers_excel.sort(key=lambda fichier: os.path.getmtime(os.path.join(chemin, fichier)), reverse=True)
        return fichiers_excel[0]

def conv_csv(fichier_recent, chemin, nom):
    # Chemin du fichier XLSX à convertir
    fichier_xlsx = rf'{chemin}\{fichier_recent}'
    # Création du fichier si il n'existe pas
    os.makedirs('C:/doc_conv/', exist_ok=True)
    # Chemin du dossier où enregistrer les fichiers CSV (assurez-vous que ce dossier existe)
    fichier_sortie = 'C:/doc_conv'
    # Lire toutes les feuilles du fichier XLSX
    sheets = pd.read_excel(fichier_xlsx, sheet_name=None)
    # Sauvegarder chaque feuille en format CSV
    for sheet_name, df in sheets.items():
        # Chemin du fichier CSV de sortie
        csv_file = f'{fichier_sortie}/{sheet_name}_{nom}.csv'
        # Sauvegarder le DataFrame en fichier CSV
        df.to_csv(csv_file, index=False)
    return fichier_sortie

def choisir_fichier_dossier(dossier):
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]

    if not fichiers:
        print("Aucun fichier trouvé dans le dossier.")
        return None

    print("Choisissez un fichier parmi la liste suivante :")
    for i, fichier in enumerate(fichiers):
        print(f"{i + 1}. {fichier}")

    while True:
        try:
            choix = int(input("Entrez le numéro du fichier choisi : "))
            if 1 <= choix <= len(fichiers):
                return fichiers[choix - 1]
            else:
                print("Numéro invalide, veuillez essayer à nouveau.")
        except ValueError:
            print("Entrée invalide, veuillez entrer un numéro valide.")

def supprimer_fichiers_dossier(dossier):
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]

    if not fichiers:
        print("Aucun fichier à supprimer dans le dossier.")
        return

    for fichier in fichiers:
        os.remove(os.path.join(dossier, fichier))

def main():
    while True:
        g = input("Que voulez-vous faire ? (extraction/connexion): ")
        if g.lower() == "extraction":
            a=input("Avez-vous un fichier xlsx ou csv (xlsx/csv): ")
            if a.lower()=="xlsx":
                a=input("Voulez-vous prendre le fichier le plus recent (oui/non): ")
                if a.lower()=="oui":
                    chemin = input(r"Entrez le chemin de votre document (attention à la casse) : ")
                    fichier_recent = fichierleplusrecent(chemin)
                    nom = input(
                        "Entrez le nom de du document (par exemple le document fait partie d'un suivi electrique vous pouvez mettre elec): ")
                    supprimer_fichiers_dossier(r"C:\doc_conv")
                    chemin_fichier_csv = conv_csv(fichier_recent, chemin, nom)
                    choix = choisir_fichier_dossier(chemin_fichier_csv)
                elif a.lower()=="non":
                    chemin = input(r"Entrez le chemin de  votre document (attention à la casse) : ")
                    fichier_recent= input("Entrez le nom de votre fichier: ")
                    nom = input(
                        "Entrez le nom de du document (par exemple le document fait partie d'un suivi electrique vous pouvez mettre elec): ")
                    supprimer_fichiers_dossier(r"C:\doc_conv")
                    chemin_fichier_csv = conv_csv(fichier_recent, chemin, nom)
                    choix = choisir_fichier_dossier(chemin_fichier_csv)
                if choix:
                    print(f"Fichier choisi : {choix}")
                    a=input("Voulez-vous continuer (oui/non): ")
                    if a.lower() == "oui":
                        print("Nous proposons plusieurs type de connection SQL. On inclut MariaDB, MySQL et InfluxDB")
                        print("InfluxDB est en fasse de test")
                        a = input("Que voulez-vous selectionner (MariaDB/MySQL/InfluxDB: ")
                        if a.lower() == "mariadb":
                            print("Le fichier vas être exporté vers une BDD MariaDB")
                            connexionMySQL_MariaDB(choix, chemin_fichier_csv)
                        elif a.lower() == "mysql":
                            print("Le fichier vas être exporté vers une BDD MySQL")
                            connexionMySQL_MariaDB(choix, chemin_fichier_csv)
                        elif a.lower() == "influxdb":
                            print("Le fichier vas être exporté vers une BDD InfluxDB")
                            connexionInfluxDB(choix, chemin_fichier_csv)
                        supprimer_fichiers_dossier("C:/doc_conv")
            elif a.lower()=="csv":
                while True:
                    a = input("Voulez-vous prendre le fichier le plus recent (oui/non/quitter): ")
                    if a.lower() == "oui":
                        chemin = input(r"Entrez le chemin de votre document (attention à la casse) : ")
                        fichier_recent = fichierleplusrecent(chemin)
                        print(rf"Voici le chemin et le nom de votre fichier: {chemin}\{fichier_recent}")
                        a = input("Voulez-vous import dans votre BDD (oui/non):")
                        if a.lower() == "oui":
                            print(
                                "Nous proposons plusieurs type de connection SQL. On inclut MariaDB, MySQL et InfluxDB")
                            print("InfluxDB est en fasse de test")
                            a = input("Que voulez-vous selectionner (MariaDB/MySQL/InfluxDB: ")
                            if a.lower() == "mariadb":
                                print("Le fichier vas être exporté vers une BDD MariaDB")
                                connexionMySQL_MariaDB(choix, chemin_fichier_csv)
                            elif a.lower() == "mysql":
                                print("Le fichier vas être exporté vers une BDD MySQL")
                                connexionMySQL_MariaDB(choix, chemin_fichier_csv)
                            elif a.lower() == "influxdb":
                                print("Le fichier vas être exporté vers une BDD InfluxDB")
                                connexionInfluxDB(choix, chemin_fichier_csv)
                            supprimer_fichiers_dossier("C:/doc_conv")
                        elif a.lower() == "non":
                            print("On recommence....")
                    elif a.lower() == "non":
                        chemin = input(r"Entrez le chemin de  votre document (attention à la casse) : ")
                        fichier = input("Entrez le nom de votre fichier: ")
                        print(rf"Voici le chemin et le nom de votre fichier: {chemin}\{fichier}")
                        a = input("Voulez-vous import dans votre BDD (oui/non):")
                        if a.lower() == "oui":
                            print(
                                "Nous proposons plusieurs type de connection SQL. On inclut MariaDB, MySQL et InfluxDB")
                            print("InfluxDB est en fasse de test")
                            a = input("Que voulez-vous selectionner (MariaDB/MySQL/InfluxDB: ")
                            if a.lower() == "mariadb":
                                print("Le fichier vas être exporté vers une BDD MariaDB")
                                connexionMySQL_MariaDB(choix, chemin_fichier_csv)
                            elif a.lower() == "mysql":
                                print("Le fichier vas être exporté vers une BDD MySQL")
                                connexionMySQL_MariaDB(choix, chemin_fichier_csv)
                            elif a.lower() == "influxdb":
                                print("Le fichier vas être exporté vers une BDD InfluxDB")
                                connexionInfluxDB(choix, chemin_fichier_csv)
                        elif a.lower() == "non":
                            print("On recommence....")
                    elif a.lower() == "quitter":
                        break
        elif g.lower() == "connexion":
            choix=None
            chemin_fichier_csv=None
            print("Nous proposons plusieurs type de connection SQL. On inclut MariaDB, MySQL et InfluxDB")
            print("InfluxDB est en fasse de test")
            a = input("Que voulez-vous selectionner (MariaDB/MySQL/InfluxDB: ")
            if a.lower() == "mariadb":
                print("Le fichier vas être exporté vers une BDD MariaDB")
                connexionMySQL_MariaDB(choix, chemin_fichier_csv)
            elif a.lower() == "mysql":
                print("Le fichier vas être exporté vers une BDD MySQL")
                connexionMySQL_MariaDB(choix, chemin_fichier_csv)
            elif a.lower() == "influxdb":
                print("Le fichier vas être exporté vers une BDD InfluxDB")
                connexionInfluxDB(choix, chemin_fichier_csv)
            supprimer_fichiers_dossier("C:/doc_conv")
        else:
            break

if __name__ == '__main__':
    main()
