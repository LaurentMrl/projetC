import pandas as pd
import os

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
