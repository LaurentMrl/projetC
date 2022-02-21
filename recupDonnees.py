import requests


def retrieveInitialCSV(csv_url : str) -> None:
    csv_url = "https://www.data.gouv.fr/fr/organizations/sante-publique-france/datasets-resources.csv"
    req = requests.get(csv_url)
    url_content = req.content
    csv_file = open('downloaded.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()