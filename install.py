import requests
import os

def add_file_by_url(chemin_destination, nom_du_fichier, url_content):
    chemin_complet = os.path.join(chemin_destination, nom_du_fichier)
    
    try:
        # Récupérer le contenu de l'URL
        reponse = requests.get(url_content)
        reponse.raise_for_status()  # Gérer les erreurs HTTP

        # Écrire le contenu dans le fichier
        with open(chemin_complet, 'wb') as fichier:
            fichier.write(reponse.content)

        print(f'Fichier créé avec succès : {chemin_complet}')
    except Exception as e:
        print(f'Erreur lors de la création du fichier : {str(e)}')

chemin_destination = 'C:/Programmes/'
nom_du_fichier = 'index.html'
url_content = 'https://raw.githubusercontent.com/VYohann/AppsPy/main/index.html'
add_file_by_url(chemin_destination, nom_du_fichier, url_content)
