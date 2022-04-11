import pandas as pd
from typing import Dict
import requests

df = pd.read_csv('initialCSV.csv', usecols=['url'], sep=';')

searchList = [["https://static.data.gouv.fr/resources/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19", "sp-pos-quot-fra"], ["https://static.data.gouv.fr/resources/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19", "sp-pos-quot-dep"], ["https://static.data.gouv.fr/resources/taux-dincidence-de-lepidemie-de-covid-19", "sp-pe-tb-quot-fra"], ["https://static.data.gouv.fr/resources/capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19", "sp-capa-quot-fra"], ["https://static.data.gouv.fr/resources/capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19", "sp-capa-quot-dep"], ["https://static.data.gouv.fr/resources/variants-circulants-indicateurs-issus-du-sequencage-emergen", "flash-fra"]]
resultList = []
names = ["donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-sp-pos-quot-fra", "donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-sp-pos-quot-dep", "taux-dincidence-de-lepidemie-de-covid-19-sp-pe-tb-quot-fra", "capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19-sp-capa-quot-fra", "capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19-sp-capa-quot-dep", "variants-circulants-indicateurs-issus-du-sequencage-emergen-flash-fra"]

for url in df["url"]:
    for goodUrl in searchList:
        if all(parts in url for parts in goodUrl):
            print(url)
            resultList.append(url)

def retrieveCSV(csv_url : str, save_name : str) -> None:
    req = requests.get(csv_url)
    url_content = req.content
    csv_file = open(f'{save_name}.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

def updateCSVs(csvUrlList : Dict[str, str]):
    for file in csvUrlList:
        retrieveCSV(csv_url = csvUrlList[file], save_name = file)

for index in range(len(resultList)):
    retrieveCSV(resultList[index-1], names[index-1])