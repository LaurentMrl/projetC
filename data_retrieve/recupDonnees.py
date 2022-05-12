import requests
import os


def retrieveCSV(csv_url: str, save_name: str) -> None:
    req = requests.get(csv_url)
    url_content = req.content
    if not os.path.exists('./ressources/csv'):
        os.makedirs('./ressources/csv')
    csv_file = open(f'./ressources/csv/{save_name}.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()


initialCsv = "https://www.data.gouv.fr/fr/organizations/sante-publique-france/datasets-resources.csv"
retrieveCSV(initialCsv, "initialCSV")