from typing import Dict
import requests

def retrieveCSV(csv_url : str, save_name : str) -> None:
    req = requests.get(csv_url)
    url_content = req.content
    csv_file = open(f'{save_name}.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

def updateCSVs(csvUrlList : Dict[str, str]):
    for file in csvUrlList:
        retrieveCSV(csv_url = csvUrlList[file], save_name = file)

initialCsv = "https://www.data.gouv.fr/fr/organizations/sante-publique-france/datasets-resources.csv"

URLCSVs = {"1" : "https://static.data.gouv.fr/resources/taux-dincidence-de-lepidemie-de-covid-19/20220306-190948/sp-pe-tb-quot-dep-2022-03-06-19h09.csv", "2" : "https://static.data.gouv.fr/resources/taux-dincidence-de-lepidemie-de-covid-19/20220306-190944/sp-pe-tb-quot-fra-2022-03-06-19h09.csv"}

retrieveCSV(initialCsv, "initialCSV")
# updateCSVs(URLCSVs)

# mydict = {"key":"value", "key2":"value2"}

# for file in mydict:
#     print(mydict[file])