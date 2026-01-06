import requests
import json

#22834958
ICO = input("Zadej ICO: ")

odkaz = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/"

adresa = odkaz + ICO

response = requests.get(adresa)
data = response.json()

print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])

klic_slovo = input("Zadej jmeno hledaneho subjektu: ")

data_2 = '{"obchodniJmeno": "XXX" }'
hledane = data_2.replace("XXX", klic_slovo)

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

odpoved = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=hledane)
seznam = odpoved.json()

pocet = int(seznam['pocetCelkem'])

for a in range(pocet):
    nazev = (seznam['ekonomickeSubjekty'][a]['obchodniJmeno'])
    cislo = (seznam['ekonomickeSubjekty'][a]['ico'])
    print(f"{nazev}, {cislo};")

data_cis = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
odpoved_cis = requests.post(" https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=data_cis)
seznam_cis = odpoved_cis.json()

ciselnik = seznam_cis["ciselniky"][0]
slovnik = ciselnik['polozkyCiselniku']

print(slovnik[1]["kod"])

def find_legal_form(hodnota, databaze):
    for polozka in databaze:
        if int(polozka["kod"]) == hodnota:
            print(polozka["nazev"])
            
zadano = int(input("Zadej kod pravni formy: "))

find_legal_form(zadano, slovnik)