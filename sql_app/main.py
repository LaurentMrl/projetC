from sqlalchemy.orm import Session
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI, Request, Depends, Response
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


env = Environment(
    loader=FileSystemLoader('templates')
)

@app.get(
    "/db/getOne_spPosQuotDep/{spPosQuotDep_id}", response_model=schemas.SpPosQuotDep
)
def readOne_spPosQuotDep(spPosQuotDep_id: int, db: Session = Depends(get_db)):
    spPosQuotDep = crud.get_spPosQuotDep(db, spPosQuotDep_id=spPosQuotDep_id)
    return spPosQuotDep


@app.get("/db/getAll_spPosQuotDep", response_model=list[schemas.SpPosQuotDep])
def readAll_spPosQuotDep(
    skip: int = 0, limit: int = 500, db: Session = Depends(get_db)
):
    spPosQuotDeps = crud.get_spPosQuotDeps(db, skip=skip, limit=limit)
    return spPosQuotDeps


@app.post("/db/create_spPosQuotDep", response_model=schemas.SpPosQuotDep)
def create_spPosQuotDep(
    spPosQuotDepCreate: schemas.SpPosQuotDepCreate, db: Session = Depends(get_db)
):
    spPosQuotDep = crud.create_spPosQuotDep(db, spPosQuotDep=spPosQuotDepCreate)
    return spPosQuotDep


@app.get("/db/getRowNumber_spPosQuotDep")
def rowNumber_spPosQuotDep(db: Session = Depends(get_db)):
    rows = db.query(models.SpPosQuotDep).count()
    return rows


@app.get(
    "/db/getOne_spPosQuotFra/{spPosQuotFra_id}", response_model=schemas.SpPosQuotFra
)
def readOne_spPosQuotFra(spPosQuotFra_id: int, db: Session = Depends(get_db)):
    spPosQuotFra = crud.get_spPosQuotFra(db, spPosQuotFra_id=spPosQuotFra_id)
    return spPosQuotFra


@app.get("/db/getAll_spPosQuotFra", response_model=list[schemas.SpPosQuotFra])
def readAll_spPosQuotFra(
    skip: int = 0, limit: int = 500, db: Session = Depends(get_db)
):
    spPosQuotFras = crud.get_spPosQuotFras(db, skip=skip, limit=limit)
    return spPosQuotFras


@app.post("/db/create_spPosQuotFra", response_model=schemas.SpPosQuotFra)
def create_spPosQuotFra(
    spPosQuotFraCreate: schemas.SpPosQuotFraCreate, db: Session = Depends(get_db)
):
    spPosQuotFra = crud.create_spPosQuotFra(db, spPosQuotFra=spPosQuotFraCreate)
    return spPosQuotFra


@app.get("/db/getRowNumber_spPosQuotFra")
def rowNumber_spPosQuotFra(db: Session = Depends(get_db)):
    rows = db.query(models.SpPosQuotFra).count()
    return rows


@app.get(
    "/db/getOne_spPeTbQuotFra/{spPeTbQuotFra_id}", response_model=schemas.SpPeTbQuotFra
)
def readOne_spPeTbQuotFra(spPeTbQuotFra_id: int, db: Session = Depends(get_db)):
    spPeTbQuotFra = crud.get_spPeTbQuotFra(db, spPeTbQuotFra_id=spPeTbQuotFra_id)
    return spPeTbQuotFra


@app.get("/db/getAll_spPeTbQuotFra", response_model=list[schemas.SpPeTbQuotFra])
def readAll_spPeTbQuotFra(
    skip: int = 0, limit: int = 500, db: Session = Depends(get_db)
):
    spPeTbQuotFras = crud.get_spPeTbQuotFras(db, skip=skip, limit=limit)
    return spPeTbQuotFras


@app.post("/db/create_spPeTbQuotFra", response_model=schemas.SpPeTbQuotFra)
def create_spPeTbQuotFra(
    spPeTbQuotFraCreate: schemas.SpPeTbQuotFraCreate, db: Session = Depends(get_db)
):
    spPeTbQuotFra = crud.create_spPeTbQuotFra(db, spPeTbQuotFra=spPeTbQuotFraCreate)
    return spPeTbQuotFra


@app.get("/db/getRowNumber_spPeTbQuotFra")
def rowNumber_spPeTbQuotFra(db: Session = Depends(get_db)):
    rows = db.query(models.SpPeTbQuotFra).count()
    return rows


@app.get(
    "/db/getOne_spPeTbQuotDep/{spPeTbQuotDep_id}", response_model=schemas.SpPeTbQuotDep
)
def readOne_spPeTbQuotDep(spPeTbQuotDep_id: int, db: Session = Depends(get_db)):
    spPeTbQuotDep = crud.get_spPeTbQuotDep(db, spPeTbQuotDep_id=spPeTbQuotDep_id)
    return spPeTbQuotDep


@app.get("/db/getAll_spPeTbQuotDep", response_model=list[schemas.SpPeTbQuotDep])
def readAll_spPeTbQuotDep(
    skip: int = 0, limit: int = 500, db: Session = Depends(get_db)
):
    spPeTbQuotDeps = crud.get_spPeTbQuotDeps(db, skip=skip, limit=limit)
    return spPeTbQuotDeps


@app.post("/db/create_spPeTbQuotDep", response_model=schemas.SpPeTbQuotDep)
def create_spPeTbQuotDep(
    spPeTbQuotDepCreate: schemas.SpPeTbQuotDepCreate, db: Session = Depends(get_db)
):
    spPeTbQuotDep = crud.create_spPeTbQuotDep(db, spPeTbQuotDep=spPeTbQuotDepCreate)
    return spPeTbQuotDep


@app.get("/db/getRowNumber_spPeTbQuotDep")
def rowNumber_spPeTbQuotDep(db: Session = Depends(get_db)):
    rows = db.query(models.SpPeTbQuotDep).count()
    return rows


@app.get(
    "/db/getOne_spCapaQuotFra/{spCapaQuotFra_id}", response_model=schemas.SpCapaQuotFra
)
def readOne_spCapaQuotFra(spCapaQuotFra_id: int, db: Session = Depends(get_db)):
    spCapaQuotFra = crud.get_spCapaQuotFra(db, spCapaQuotFra_id=spCapaQuotFra_id)
    return spCapaQuotFra


@app.get("/db/getAll_spCapaQuotFra", response_model=list[schemas.SpCapaQuotFra])
def readAll_spPeTbQuotDep(
    skip: int = 0, limit: int = 500, db: Session = Depends(get_db)
):
    spCapaQuotFras = crud.get_spCapaQuotFras(db, skip=skip, limit=limit)
    return spCapaQuotFras


@app.post("/db/create_spCapaQuotFra", response_model=schemas.SpCapaQuotFra)
def create_spCapaQuotFra(
    spCapaQuotFraCreate: schemas.SpCapaQuotFraCreate, db: Session = Depends(get_db)
):
    spCapaQuotFra = crud.create_spCapaQuotFra(db, spCapaQuotFra=spCapaQuotFraCreate)
    return spCapaQuotFra


@app.get("/db/getRowNumber_spCapaQuotFra")
def rowNumber_spCapaQuotFra(db: Session = Depends(get_db)):
    rows = db.query(models.SpCapaQuotFra).count()
    return rows


@app.get(
    "/db/getOne_spCapaQuotDep/{spCapaQuotDep_id}", response_model=schemas.SpCapaQuotDep
)
def readOne_spCapaQuotDep(spCapaQuotDep_id: int, db: Session = Depends(get_db)):
    spCapaQuotDep = crud.get_spCapaQuotDep(db, spCapaQuotDep_id=spCapaQuotDep_id)
    return spCapaQuotDep


@app.get("/db/getAll_spCapaQuotDep", response_model=list[schemas.SpCapaQuotDep])
def readAll_spCapaQuotDep(
    skip: int = 0, limit: int = 500, db: Session = Depends(get_db)
):
    spCapaQuotDeps = crud.get_spCapaQuotDeps(db, skip=skip, limit=limit)
    return spCapaQuotDeps


@app.post("/db/create_spCapaQuotDep", response_model=schemas.SpCapaQuotDep)
def create_spCapaQuotDep(
    spCapaQuotDepCreate: schemas.SpCapaQuotDepCreate, db: Session = Depends(get_db)
):
    spCapaQuotDep = crud.create_spCapaQuotDep(db, spCapaQuotDep=spCapaQuotDepCreate)
    return spCapaQuotDep


@app.get("/db/getRowNumber_spCapaQuotDep")
def rowNumber_spCapaQuotDep(db: Session = Depends(get_db)):
    rows = db.query(models.SpCapaQuotDep).count()
    return rows


@app.get("/db/getOne_flashFra/{flashFra_id}", response_model=schemas.FlashFra)
def readOne_flashFra(flashFra_id: int, db: Session = Depends(get_db)):
    flashFra = crud.get_flashFra(db, flashFra_id=flashFra_id)
    return flashFra


@app.get("/db/getAll_flashFra", response_model=list[schemas.FlashFra])
def readAll_flashFra(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    flashFras = crud.get_flashFras(db, skip=skip, limit=limit)
    return flashFras


@app.post("/db/create_flashFra", response_model=schemas.FlashFra)
def create_flashFra(
    flashFraCreate: schemas.FlashFraCreate, db: Session = Depends(get_db)
):
    flashFra = crud.create_flashFra(db, flashFra=flashFraCreate)
    return flashFra


@app.get("/db/getRowNumber_flashFra")
def rowNumber_flashFra(db: Session = Depends(get_db)):
    rows = db.query(models.FlashFra).count()
    return rows

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
    template = env.get_template("../web/templates/index.html")
    template.render(graphique_femme=graphique_femme, graphique_homme=graphique_homme, graphique=graphique, graphique_variant=graphique_variant )