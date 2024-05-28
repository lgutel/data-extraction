import mysql.connector
import csv
def connexionsql():
    db = mysql.connector.connect(
        host=input("Entrez l'@ip de votre serveur: "),
        user=input("Entrez votre login: "),
        password=input("Entrez votre password: "),
        database=input("Entrez votre Base de Données: ")
    )
    # Créez un curseur pour exécuter des requêtes
    cursor = db.cursor()
    database =db.database
    a=input("Voulez-vous passer en manuel ou en automatique? (auto/manu)")
    if a.lower() == "manu":
        while True:
            b=input("Voulez vous lire, écrire ou quitter: ")
            if b=="lire":
                table = input("Entrez le nom de votre table: ")
                # Exécutez la requête SQL
                query = f"SELECT * FROM {table}"
                cursor.execute(query)
                # Récupérez les résultats
                result = cursor.fetchall()
                # Affichez chaque ligne de résultat
                for row in result:
                    print(row)
            elif b=="écrire":
                print("Attention ceci est réservé pour les personnes qui si connaisse")
                print("Pour l'écriture, voulez-vous ajouter un table ou ajouter des données ")
                c=input("Ecrivez: Cas1 pour ajouter la table ou Cas2 pour ajouter les données ")
                if c.lower() == "cas1":
                    while True:
                        # Ajout de table dans la BDD
                        nomdetable = input("Entrez le nom de la table à ajouter: ")
                        colonne = input(
                            "Entrez les colonnes à ajouter (par exemple: 'nom VARCHAR(100), prenom VARCHAR(100), date_naissance DATE'): ")

                        # Création de la requête SQL
                        query = f"CREATE TABLE {nomdetable} (id INT PRIMARY KEY AUTO_INCREMENT, {colonne})"
                        print(query)

                        d = input("Voulez-vous exécuter la commande ? (oui/non) ")
                        if d.lower() == "oui":
                            try:
                                cursor.execute(query)
                                db.commit()
                                print(f"Table {nomdetable} ajoutée avec succès.")
                                break  # Sortir de la boucle si la commande a été exécutée avec succès
                            except mysql.connector.Error as err:
                                print(f"Erreur: {err}")
                        else:
                            print("Recommençons la saisie des informations.")
                            r=input("Voulez-vous continuer ? (oui/non)")
                            if r.lower() == "non":
                                break
                elif c.lower() == "cas2":
                    while True:
                        # Ajout de données dans la BDD
                        nomdetable = input("Entrez le nom de la table où ajouter des données: ")
                        colonnes = input("Entrez les noms des colonnes (par exemple: 'nom, prenom, date_naissance'): ")
                        valeurs = input("Entrez les valeurs à insérer (par exemple: 'John, Doe, 1980-01-01'): ")

                        # Traitement des valeurs
                        valeurs = ', '.join(f"'{v.strip()}'" for v in valeurs.split(','))

                        # Création de la requête SQL
                        query = f"INSERT INTO {nomdetable} ({colonnes}) VALUES ({valeurs})"
                        print(query)

                        d = input("Voulez-vous exécuter la commande ? (oui/non) ")
                        if d.lower() == "oui":
                            try:
                                cursor.execute(query)
                                db.commit()
                                print(f"Données ajoutées à la table {nomdetable} avec succès.")
                                break  # Sortir de la boucle si la commande a été exécutée avec succès
                            except mysql.connector.Error as err:
                                print(f"Erreur: {err}")
                                print("Recommençons la saisie des informations.")
                        else:
                            print("Recommençons la saisie des informations.")
                            r = input("Voulez-vous continuer ? (oui/non)")
                            if r.lower() == "non":
                                break
            elif b.lower() == "quitter":
                # Fermeture du curseur et de la connexion
                cursor.close()
                db.close()
                print("Vous avez quitté avec succès")
                break
    elif a.lower() == "auto":
        while True:
            b=input("Voulez-vous sauvegarder les ancienne tables (oui/non)")
            if b.lower() == "oui":
                tables_to_export = input("Entrez les noms des tables à exporter, séparés par des virgules: ").split(',')
                for table in tables_to_export:
                    file_name = f"{table.strip()}.csv"
                    try:
                        query = f"SELECT * FROM {table.strip()}"
                        cursor.execute(query)
                        rows = cursor.fetchall()
                        columns = [i[0] for i in cursor.description]

                        with open(file_name, mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(columns)  # Écrire les en-têtes de colonnes
                            writer.writerows(rows)  # Écrire les données

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
                except mysql.connector.Error as err:
                    print(f"Erreur: {err}")
