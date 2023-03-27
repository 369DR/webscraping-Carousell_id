import bs4
import requests

url = "https://id.carousell.com/u/carousell_id/"
abundance = requests.get(url)
#print(abundance.text)

response = bs4.BeautifulSoup(abundance.text, "html.parser")
#print(response)
data = response.find_all("div", "D_aje M_abw")
print(data[0].text)
