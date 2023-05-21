import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--title", required=True)
parser.add_argument("-f", "--file", required=True)
parser.add_argument("-u", "--username", required=True)
parser.add_argument("-p", "--password", required=True)
args = parser.parse_args()

login_data = {"username": args.username, "password": args.password}
server = "http://127.0.0.1:8000"

with requests.Session() as s:
    s.get(server + "/admin/login/")
    login_data["csrfmiddlewaretoken"] = s.cookies["csrftoken"]
    s.post(server + "/admin/login/", data=login_data)
    cocktail_url = f"{server}/cocktails-by-title/{args.title}/"
    cocktail = s.get(cocktail_url).json()

    if cocktail:
        update_url = f'{server}/cocktail-update/{cocktail[0]["pk"]}/'
        update_form_page = s.get(update_url)
        soup = BeautifulSoup(update_form_page.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})[
            "value"
        ]
        form_data = {
            "title": args.title,
            "image_title": args.title,
            "csrfmiddlewaretoken": csrf_token
        }
        with open(args.file, "rb") as img_file:
            file_data = {"file": img_file}
            r = s.post(update_url, data=form_data, files=file_data)

        if r.status_code == 200:
            print(f"Cocktail '{args.title}' updated!")
        else:
            print(f"Error updating cocktail '{args.title}'.")
    else:
        print(f"No cocktail found with the title '{args.title}'")
