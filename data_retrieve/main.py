"""
Un truc qui import tout et lance la récup des données
"""
import os
import pandas as pd
import recupDonnees
import getCSVURL
import convertToJson


BASE_SITE = "https://www.data.gouv.fr"
initialCsv = (
    f"{BASE_SITE}/fr/organizations/sante-publique-france/datasets-resources.csv"
)
recupDonnees.retrieveCSV(initialCsv, "initialCSV")


for index in range(len(getCSVURL.resultList)):
    getCSVURL.retrieveCSV(getCSVURL.resultList[index - 1], getCSVURL.names[index - 1])


for file in convertToJson.files:
    csvFullFile = f"./ressources/csv/{file}.csv"
    if not os.path.exists("./ressources/json"):
        os.makedirs("./ressources/json")
    jsonFullFile = f"./ressources/json/{file}.json"
    df = pd.read_csv(csvFullFile)
    df.to_json(jsonFullFile)
