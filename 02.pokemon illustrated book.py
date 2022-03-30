import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

res = requests.get ("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
soup = BeautifulSoup(res.text, "html.parser")

for i in soup.select(".pokemonicon"):
    이름 = i.select_one(".pokemonname").text
    링크 = "https:" + i.select_one("img").get("src").replace("pokemonicon","pokemonimage")
    r = requests.get(링크)
    f = open(f"포켓몬/{이름}.png","wb") 
    f.write(r.content)
    f.close()