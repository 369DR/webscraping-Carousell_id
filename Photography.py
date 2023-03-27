from bs4 import BeautifulSoup
import requests

html_doc = requests.get ("https://id.carousell.com/categories/photography-6/")
soup = BeautifulSoup(html_doc.text, "html.parser")

kamera_terpopuler = soup.find(attrs={"class": "D_J asm-browse-listings"})


titles = kamera_terpopuler.findAll(attrs={"class":"listing-card-1223024372"})

for title in titles:
    # print(title.text)
    print(title.find('p',attrs={'class':'D_rw M_nF D_ri M_lT D_rx M_nG D_rA M_nK D_rE M_nN D_rH M_nQ D_rJ M_nS D_rF M_nO D_rN'}).text)