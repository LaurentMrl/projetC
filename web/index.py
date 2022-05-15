import pandas as pd
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI, Request, Depends, Response
from .database import SessionLocal, engine
env = Environment(
    loader=FileSystemLoader('templates')
)


@app.route('/index', methods=("POST", "GET"))
async def graphique(request: Request):
    donnees = pd.read_sql_query("SELECT * FROM sp_pos_quot_fra", con=engine)
    graphique_femme = plt.plot(donnees.jour, donnees.T_f, c="blue", marker=",")
    plt.plot(donnees.jour, donnees.P_f, c="red", marker=",")
    plt.xticks(np.arange(0, donnees.jour.unique().size, 30), rotation=90)
    plt.xlabel("Jour")
    plt.ylabel("Nombre de cas de Covid chez les femmes en fonction du nombre de Tests")
    plt.legend(['Test', 'Positif'])
    plt.title("Evolution du nombre de cas de Covid chez les femmes par rapport au tests en fonction du temps.",
              loc='left')

    graphique_homme = plt.plot(donnees.jour, donnees.T_h, c="blue", marker=",")
    plt.plot(donnees.jour, donnees.P_h, c="red", marker=",")
    plt.xticks(np.arange(0, donnees.jour.unique().size, 30), rotation=90)
    plt.xlabel("Jour")
    plt.ylabel("Nombre de cas de Covid chez les hommes en fonction du nombre de Tests")
    plt.legend(['Test', 'Positif'])
    plt.title("Evolution du nombre de cas de Covid chez les hommes par rapport au tests en fonction du temps.",
              loc='left')
    graphique = plt.plot(donnees.jour, donnees.T, c="blue", marker=",")
    plt.plot(donnees.jour, donnees.P, c="red", marker=",")
    plt.xticks(np.arange(0, donnees.jour.unique().size, 30), rotation=90)
    plt.xlabel("Jour")
    plt.ylabel("Nombre de cas de Covid en fonction du nombre de Tests")
    plt.legend(['Test', 'Positif'])
    plt.title("Evolution du nombre de cas de Covid par rapport au tests en fonction du temps.", loc='left')

    donnees_variant = pd.read_sql_query("SELECT * FROM flash_fra", con=engine)

    graphique_variant = plt.plot(donnees_variant.deb_periode, donnees_variant.n_tot, c="black", marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 1]['n'],
             c='yellow', marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 2]['n'],
             c='orange', marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 3]['n'],
             c='brown', marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 4]['n'],
             c='red', marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 5]['n'],
             c='green', marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 6]['n'],
             c='blue', marker=",")
    plt.plot(donnees_variant.deb_periode.unique(), donnees_variant[donnees_variant['flash_variants'] == 7]['n'],
             c='grey', marker=",")
    plt.xticks(np.arange(0, donnees_variant.deb_periode.unique().size, 2), rotation=90)
    plt.xlabel("Jour")
    plt.ylabel("Nombre de cas de Covid par variant.")
    plt.legend(['Total', 'Alpha', 'B.1.640', 'Beta', 'Delta', 'Gamma', 'Omicron', 'Autres variants'])
    plt.title("Evolution du nombre de cas de Covid par variants en fonction du temps.")
    template = env.get_template("index.html")
    print(template.render(graphique_femme=graphique_femme, graphique_homme=graphique_homme, graphique=graphique, graphique_variant=graphique_variant ))