import pandas as pd
import os

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

def main():
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
        print(feuille)

if __name__=='__main__':
    main()