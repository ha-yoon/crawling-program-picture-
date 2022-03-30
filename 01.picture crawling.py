#네이버에서 사진 가져오기
import requests

res = requests.get("") 

f = open("kennen.png","wb") 
f.write(res.content)
f.close()


#마저자르기
from bs4 import BeautifulSoup

st = """
<html>
    <body>
        <div class="champ">
            <div id="name">kennen</div>
            <div id="hp">1000</div>
            <div id="mp">500</div>
        </div>
        <div class="champ">
            <div id="name">timo</div>
            <div id="hp">300</div>
            <div id="mp">200</div>
        </div>
        <div class="champ">
            <div id="name">veigar</div>
            <div id="hp">200</div>
            <div id="mp">1000</div>
        </div>
    </body>
</html>"""

soup = BeautifulSoup(st, "html.parser")




