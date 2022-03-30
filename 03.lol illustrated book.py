import os
import requests
from bs4 import BeautifulSoup


def 파일유효값전환(st):
    for i in "\\/<>.\"?!":
        st = st.replace(i, "")
    return st

def 폴더생성(A):
    if os.path.isdir(A):
        pass
    else:
        os.mkdir(A)

폴더생성("lol")

res = requests.get("https://lol.inven.co.kr/dataninfo/champion/")
soup = BeautifulSoup(res.text, "html.parser")

# key : 이름, value : 코드
롤 = {}
for i in soup.select(".champImage > a"):
    이름 = 파일유효값전환(i.get("title"))
    코드 = i.get("href")[16:]   
    롤[이름] = 코드


for k in 롤:

    폴더생성(f"lol/{k}")

    res = requests.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={롤[k]}")
    soup = BeautifulSoup(res.text, "html.parser")

    # 스킨이름, 사진경로
    링크들 = []
    for i in soup.select(".askin > img"):
        링크 = i.get("src")
        링크들.append(링크)

    파일이름 = []
    for i in soup.select(".askinname")[::2]:
        파일이름.append(파일유효값전환(i.text.split("-")[0]))

    for i in range(len(링크들)):
        r = requests.get(링크들[i])
        f = open(f"lol/{k}/{파일이름[i]}.png", "wb")
        f.write(r.content)
        f.close()