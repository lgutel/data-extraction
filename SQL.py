import mysql.connector
from mysql.connector import errorcode
import csv
import os
import pandas as pd


def connexionsql(choix, chemin_fichier_csv):
    db = mysql.connector.connect(
        host=input("Entrez l'@ip de votre serveur: "),
        user=input("Entrez votre login: "),
        password=input("Entrez votre password: "),
        database=input("Entrez votre Base de Données: ")
    )
    cursor = db.cursor()
    database = db.database

    while True:
        a = input("Voulez-vous passer en manuel ou en automatique? (auto/manu/quitter): ")
        if a.lower() == "manu":
            while True:
                b = input("Voulez-vous lire, écrire ou quitter: ")
                if b.lower() == "lire":
                    table = input("Entrez le nom de votre table: ")
                    query = f"SELECT * FROM {table}"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                elif b.lower() == "écrire":
                    print("Attention ceci est réservé pour les personnes qui s'y connaissent")
                    print("Pour l'écriture, voulez-vous ajouter une table ou ajouter des données?")
                    c = input("Écrivez: Cas1 pour ajouter la table ou Cas2 pour ajouter les données: ")
                    if c.lower() == "cas1":
                        while True:
                            nomdetable = input("Entrez le nom de la table à ajouter: ")
                            colonne = input(
                                "Entrez les colonnes à ajouter (par exemple: 'nom VARCHAR(100), prenom VARCHAR(100), date_naissance DATE'): ")
                            query = f"CREATE TABLE {nomdetable} (id INT PRIMARY KEY AUTO_INCREMENT, {colonne})"
                            print(query)
                            d = input("Voulez-vous exécuter la commande ? (oui/non): ")
                            if d.lower() == "oui":
                                try:
                                    cursor.execute(query)
                                    db.commit()
                                    print(f"Table {nomdetable} ajoutée avec succès.")
                                    break
                                except mysql.connector.Error as err:
                                    print(f"Erreur: {err}")
                            else:
                                print("Recommençons la saisie des informations.")
                                r = input("Voulez-vous continuer ? (oui/non): ")
                                if r.lower() == "non":
                                    break
                    elif c.lower() == "cas2":
                        while True:
                            nomdetable = input("Entrez le nom de la table où ajouter des données: ")
                            colonnes = input(
                                "Entrez les noms des colonnes (par exemple: 'nom, prenom, date_naissance'): ")
                            valeurs = input("Entrez les valeurs à insérer (par exemple: 'John, Doe, 1980-01-01'): ")
                            valeurs = ', '.join(f"'{v.strip()}'" for v in valeurs.split(','))
                            query = f"INSERT INTO {nomdetable} ({colonnes}) VALUES ({valeurs})"
                            print(query)
                            d = input("Voulez-vous exécuter la commande ? (oui/non): ")
                            if d.lower() == "oui":
                                try:
                                    cursor.execute(query)
                                    db.commit()
                                    print(f"Données ajoutées à la table {nomdetable} avec succès.")
                                    break
                                except mysql.connector.Error as err:
                                    print(f"Erreur: {err}")
                                    print("Recommençons la saisie des informations.")
                            else:
                                print("Recommençons la saisie des informations.")
                                r = input("Voulez-vous continuer ? (oui/non): ")
                                if r.lower() == "non":
                                    break
                    elif b.lower() == "quitter":
                        break

        elif a.lower() == "auto" and choix is not None:
            while True:
                print(
                    "La fonction de sauvegarde des anciennes tables ne fonctionne qu'à moitié. Je vous propose d'enregistrer vos tables directement sur place. Merci :/")
                b = input("Voulez-vous sauvegarder les anciennes tables (oui/non/quitter): ")
                if b.lower() == "oui":
                    tables_to_export = input("Entrez les noms des tables à exporter, séparés par des virgules: ").split(
                        ',')
                    for table in tables_to_export:
                        file_name = f"{table.strip()}.csv"
                        try:
                            query = f"SELECT * FROM {table.strip()}"
                            cursor.execute(query)
                            rows = cursor.fetchall()
                            columns = [i[0] for i in cursor.description]
                            with open(file_name, mode='w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(columns)
                                writer.writerows(rows)
                            print(
                                f"Les données de la table {table.strip()} ont été exportées avec succès dans le fichier {file_name}.")
                        except mysql.connector.Error as err:
                            print(f"Erreur: {err}")

                elif b.lower() == "non":
                    try:
                        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
                        cursor.execute(

                            f"SELECT CONCAT('DROP TABLE IF EXISTS `', table_name, '`;') FROM information_schema.tables WHERE table_schema = '{database}';")
                        drop_table_queries = cursor.fetchall()
                        for drop_query in drop_table_queries:
                            cursor.execute(drop_query[0])
                        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
                        db.commit()
                        print("Toutes les tables ont été supprimées avec succès.")
                        chemin_fichier_csv=rf"{chemin_fichier_csv}\{choix}"
                        ## Compter le nombre de colonnes pour créer la table
                        with open(chemin_fichier_csv, newline='') as csvfile:
                            reader = csv.reader(csvfile)
                            num_columns = len(next(reader))
                        ## Créer la requête pour créer la table
                        table_name = os.path.splitext(os.path.basename(chemin_fichier_csv))[0]
                        create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("
                        for i in range(num_columns):
                            create_table_query += f"colonne_{i} VARCHAR(255), "
                        create_table_query = create_table_query.rstrip(', ') + ")"
                        cursor.execute(create_table_query)
                        db.commit()
                        print(f"La table `{table_name}` a été créée avec succès.")
                        ## Insérer les données du CSV dans la table
                        with open(chemin_fichier_csv, newline='') as csvfile:
                            csv_data = csv.reader(csvfile)
                            next(csv_data)  # Skip header
                            for row in csv_data:
                                cursor.execute(f"INSERT INTO `{table_name}` VALUES ({', '.join(['%s'] * num_columns)})",
                                               row)
                            db.commit()
                            print(f"Données importées avec succès dans la table `{table_name}`.")
                    except mysql.connector.Error as err:
                        print(f"Erreur: {err}")
                elif b.lower() == "quitter":
                    break

        elif a.lower() == "quitter":
            cursor.close()
            db.close()
            print("Vous avez quitté avec succès")
            break
