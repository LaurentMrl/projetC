"""
Un truc qui import tout et lance la récup des données
"""
import os
import pandas as pd
import recupDonnees
import getCSVURL

BASE_SITE = "https://www.data.gouv.fr"
initialCsv = (
    f"{BASE_SITE}/fr/organizations/sante-publique-france/datasets-resources.csv"
)
recupDonnees.retrieveCSV(initialCsv, "initialCSV")


for index in range(len(getCSVURL.resultList)):
    getCSVURL.retrieveCSV(getCSVURL.resultList[index - 1], getCSVURL.names[index - 1])

files = [
    "capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19-sp-capa-quot-dep",
    "capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19-sp-capa-quot-fra",
    "donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-sp-pos-quot-dep",
    "donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-sp-pos-quot-fra",
    "taux-dincidence-de-lepidemie-de-covid-19-sp-pe-tb-quot-fra",
    "variants-circulants-indicateurs-issus-du-sequencage-emergen-flash-fra",
]


for file in files:
    csvFullFile = f"./ressources/csv/{file}.csv"
    if not os.path.exists("./ressources/json"):
        os.makedirs("./ressources/json")
    jsonFullFile = f"./ressources/json/{file}.json"
    df = pd.read_csv(csvFullFile)
    df.to_json(jsonFullFile)
