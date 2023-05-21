import argparse
import requests
from bs4 import BeautifulSoup

login_url = "http://127.0.0.1:8000/login/"

parser = argparse.ArgumentParser(
    description="Upload an image for a given cocktail."
)
parser.add_argument("-t", "--title", required=True)
parser.add_argument("-f", "--file", required=True)
parser.add_argument("-u", "--username", required=True)
parser.add_argument("-p", "--password", required=True)
args = parser.parse_args()

login_data = {"username": args.username, "password": args.password}
server = "http://127.0.0.1:8000"
with requests.Session() as s:
    s.get(login_url)
    login_data["csrfmiddlewaretoken"] = s.cookies["csrftoken"]
    s.post(login_url, data=login_data)
    cocktail_url = f"{server}/cocktails-by-title/{args.title}/"
    cocktail = s.get(cocktail_url).json()

    if cocktail:
        update_url = f'{server}/cocktail-update/{cocktail[0]["pk"]}/'
        form_data = {
            "title": args.title,
            "csrfmiddlewaretoken": s.cookies["csrftoken"],
        }
        file_data = {"image": open(args.file, "rb")}
        r = s.post(update_url, data=form_data, files=file_data)

        if r.status_code == 200:
            print("Cocktail mis à jour avec succès.")
        else:
            print("Erreur lors de la mise à jour du cocktail.")
    else:
        print("Aucun cocktail trouvé avec ce titre.")
