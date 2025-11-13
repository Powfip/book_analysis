import requests
from bs4 import BeautifulSoup
import pandas as pd
libros = []
for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    for libro in soup.select(".product_pod"):
        titulo = libro.h3.a["title"]
        precio = libro.select_one(".price_color").text
        rating = libro.p["class"][1]
        disponibilidad = libro.select_one(".instock.availability").text.strip()
        libros.append({
            "titulo": titulo,
            "precio": precio,
            "rating": rating,
            "disponibilidad": disponibilidad
        })

df = pd.DataFrame(libros)
df.to_csv("libros.csv", index=False)