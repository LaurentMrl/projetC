import pandas as pd

files = ["capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19-sp-capa-quot-dep", "capacite-analytique-de-tests-virologiques-dans-le-cadre-de-lepidemie-covid-19-sp-capa-quot-fra", "donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-sp-pos-quot-dep", "donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-sp-pos-quot-fra", "taux-dincidence-de-lepidemie-de-covid-19-sp-pe-tb-quot-fra", "variants-circulants-indicateurs-issus-du-sequencage-emergen-flash-fra"]

for file in files :
    csvFullFile = f"{file}.csv"
    jsonFullFile = f"{file}.json"
    df = pd.read_csv (csvFullFile)
    df.to_json (jsonFullFile)