import pandas as pd
import os
import mysql.connector

def fichierleplusrecent(chemin):
    # Obtenez la liste des fichiers Excel dans le répertoire spécifié
    fichiers_excel = [fichier for fichier in os.listdir(chemin) if fichier.lower().endswith(".xlsx")]

    if not fichiers_excel:
        print("Aucun fichier Excel trouvé dans le répertoire spécifié.")
    else:
        # Triez les fichiers par date de modification (le plus récent en premier)
        fichiers_excel.sort(key=lambda fichier: os.path.getmtime(os.path.join(chemin, fichier)), reverse=True)

        # Sélectionnez le fichier le plus récent
        return fichiers_excel[0]

def nomfeuille(chemin, fichier_recent): #liste les nom des différentes feuilles

    # Chargez le classeur Excel
    excel_file_path = os.path.join(chemin, fichier_recent)
    xl = pd.ExcelFile(excel_file_path)

    # Obtenez la liste des noms de feuilles
    sheet_names = xl.sheet_names
    print("Voici une liste des nom de feuille : ")
    for sheet_name in sheet_names:
        print(f"- {sheet_name}")

def connexionsql():
    db = mysql.connector.connect(
        host=input("Entrez l'@ip de votre serveur: "),
        user=input("Entrez votre login: "),
        password=input("Entrez votre password: "),
        database=input("Entrez votre Base de Données: ")
    )
    # Créez un curseur pour exécuter des requêtes
    cursor = db.cursor()
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
def main():
    while True:
        g=input("Que voulez-vous faire ? (extraction/connexion)")
        if g.lower() == "extraction":
            chemin = input(r"Entrez le chemin de votre documents (attention sensible à la case) : ")
            fichier_recent=fichierleplusrecent(chemin)
            a = input("Est-ce il y a plusieurs feuilles dans ce document : ")
            #si il y a plusieurs feuilles dans le doc excel le liste et l'utilisateur choisi
            if a == 'oui':
                nomfeuille(chemin, fichier_recent)
                feuille = input("Entrez le nom de la feuille à extraire : ")
                try:
                    df=pd.read_excel(fichier_recent, sheet_name=feuille)
                    print("Données extraites de la feuille sélectionnée :")
                    print(df)
                except Exception as e:
                    print(f"Erreur lors de l'extraction des données : {e}")
            else:
                feuille = input("Entrez le nom de la feuille à extraire : ")
                try:
                    df = pd.read_excel(fichier_recent, sheet_name=feuille)
                    print("Données extraites de la feuille sélectionnée :")
                    print(df)
                except Exception as e:
                    print(f"Erreur lors de l'extraction des données : {e}")

        elif g.lower() == "connexion":
            connexionsql()
        else:
            break

if __name__=='__main__':
    main()
