import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

parser = argparse.ArgumentParser(
    description="Extract images and titles from URLs."
)
parser.add_argument(
    "-f",
    "--file",
    required=True,
    help="The name of the file containing the URLs.",
)
parser.add_argument(
    "-u", "--username", required=True, help="The username for authentication."
)
parser.add_argument(
    "-p", "--password", required=True, help="The password for authentication."
)
parser.add_argument(
    "-d",
    "--destination",
    required=True,
    help="The destination directory for downloaded images.",
)

args = parser.parse_args()

with open(args.file, "r") as f:
    urls = f.readlines()

to_do = 5
for url in urls:
    url = url.strip()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    figure = soup.find("figure", {"class": "custom item-image"})
    h1 = soup.find("h1", itemprop="headline")

    if figure and h1:
        img = figure.find("img")
        if img:
            img_src = urljoin(url, img.get("src"))
            title = h1.find("span", itemprop="name").text
            if title.lower().startswith("cocktail"):
                title = title[9:]

            img_response = requests.get(img_src)
            img_data = img_response.content
            image_file_path = os.path.join(
                args.destination, f"{title.replace('/', '_')}.jpg"
            )

            with open(image_file_path, "wb") as img_file:
                img_file.write(img_data)

            print(
                f"python update_cocktail.py "
                f"-u {args.username} "
                f"-p {args.password} "
                f"-t '{title}' "
                f"-f '{image_file_path}'"
            )
    to_do -= 1
    # if to_do == 0:
    #     break
