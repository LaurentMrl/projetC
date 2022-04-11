from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

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


@app.get("/db/getOne_spPosQuotDep/{spPosQuotDep_id}", response_model=schemas.SpPosQuotDep)
def readOne_spPosQuotDep(spPosQuotDep_id: int, db: Session = Depends(get_db)):
    spPosQuotDep = crud.get_spPosQuotDep(db, spPosQuotDep_id=spPosQuotDep_id)
    return spPosQuotDep


@app.get("/db/getAll_spPosQuotDep", response_model=list[schemas.SpPosQuotDep])
def readAll_spPosQuotDep(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    spPosQuotDeps = crud.get_spPosQuotDeps(db, skip=skip, limit=limit)
    return spPosQuotDeps


@app.post("/db/create_spPosQuotDep", response_model=schemas.SpPosQuotDep)
def create_spPosQuotDep(spPosQuotDepCreate: schemas.SpPosQuotDepCreate, db: Session = Depends(get_db)):
    spPosQuotDep = crud.create_spPosQuotDep(db, spPosQuotDep=spPosQuotDepCreate)
    return spPosQuotDep


@app.get("/db/getRowNumber_spPosQuotDep")
def rowNumber_spPosQuotDep(db: Session = Depends(get_db)):
    rows = db.query(models.SpPosQuotDep).count()
    return rows


@app.get("/db/getOne_spPeTbQuotFra/{spPeTbQuotFra_id}", response_model=schemas.SpPeTbQuotFra)
def readOne_spPeTbQuotFra(spPeTbQuotFra_id: int, db: Session = Depends(get_db)):
    spPeTbQuotFra = crud.get_spPeTbQuotFra(db, spPeTbQuotFra_id=spPeTbQuotFra_id)
    return spPeTbQuotFra


@app.get("/db/getAll_spPeTbQuotFra", response_model=list[schemas.SpPeTbQuotFra])
def readAll_spPeTbQuotFra(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    spPeTbQuotFras = crud.get_spPeTbQuotFras(db, skip=skip, limit=limit)
    return spPeTbQuotFras


@app.post("/db/create_spPeTbQuotFra", response_model=schemas.SpPeTbQuotFra)
def create_spPeTbQuotFra(spPeTbQuotFraCreate: schemas.SpPeTbQuotFraCreate, db: Session = Depends(get_db)):
    spPeTbQuotFra = crud.create_spPeTbQuotFra(db, spPeTbQuotFra=spPeTbQuotFraCreate)
    return spPeTbQuotFra


@app.get("/db/getRowNumber_spPeTbQuotFra")
def rowNumber_spPeTbQuotFra(db: Session = Depends(get_db)):
    rows = db.query(models.SpPeTbQuotFra).count()
    return rows


@app.get("/db/getOne_spPeTbQuotDep/{spPeTbQuotDep_id}", response_model=schemas.SpPeTbQuotDep)
def readOne_spPeTbQuotDep(spPeTbQuotDep_id: int, db: Session = Depends(get_db)):
    spPeTbQuotDep = crud.get_spPeTbQuotDep(db, spPeTbQuotDep_id=spPeTbQuotDep_id)
    return spPeTbQuotDep


@app.get("/db/getAll_spPeTbQuotDep", response_model=list[schemas.SpPeTbQuotDep])
def readAll_spPeTbQuotDep(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    spPeTbQuotDeps = crud.get_spPeTbQuotDeps(db, skip=skip, limit=limit)
    return spPeTbQuotDeps


@app.post("/db/create_spPeTbQuotDep", response_model=schemas.SpPeTbQuotDep)
def create_spPeTbQuotDep(spPeTbQuotDepCreate: schemas.SpPeTbQuotDepCreate, db: Session = Depends(get_db)):
    spPeTbQuotDep = crud.create_spPeTbQuotDep(db, spPeTbQuotDep=spPeTbQuotDepCreate)
    return spPeTbQuotDep


@app.get("/db/getRowNumber_spPeTbQuotDep")
def rowNumber_spPeTbQuotDep(db: Session = Depends(get_db)):
    rows = db.query(models.SpPeTbQuotDep).count()
    return rows


@app.get("/db/getOne_spCapaQuotFra/{spCapaQuotFra_id}", response_model=schemas.SpCapaQuotFra)
def readOne_spCapaQuotFra(spCapaQuotFra_id: int, db: Session = Depends(get_db)):
    spCapaQuotFra = crud.get_spCapaQuotFra(db, spCapaQuotFra_id=spCapaQuotFra_id)
    return spCapaQuotFra


@app.get("/db/getAll_spCapaQuotFra", response_model=list[schemas.SpCapaQuotFra])
def readAll_spPeTbQuotDep(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    spCapaQuotFras = crud.get_spCapaQuotFras(db, skip=skip, limit=limit)
    return spCapaQuotFras


@app.post("/db/create_spCapaQuotFra", response_model=schemas.SpCapaQuotFra)
def create_spCapaQuotFra(spCapaQuotFraCreate: schemas.SpCapaQuotFraCreate, db: Session = Depends(get_db)):
    spCapaQuotFra = crud.create_spCapaQuotFra(db, spCapaQuotFra=spCapaQuotFraCreate)
    return spCapaQuotFra


@app.get("/db/getRowNumber_spCapaQuotFra")
def rowNumber_spCapaQuotFra(db: Session = Depends(get_db)):
    rows = db.query(models.SpCapaQuotFra).count()
    return rows


@app.get("/db/getOne_spCapaQuotDep/{spCapaQuotDep_id}", response_model=schemas.SpCapaQuotDep)
def readOne_spCapaQuotDep(spCapaQuotDep_id: int, db: Session = Depends(get_db)):
    spCapaQuotDep = crud.get_spCapaQuotDep(db, spCapaQuotDep_id=spCapaQuotDep_id)
    return spCapaQuotDep


@app.get("/db/getAll_spCapaQuotDep", response_model=list[schemas.SpCapaQuotDep])
def readAll_spCapaQuotDep(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    spCapaQuotDeps = crud.get_spCapaQuotDeps(db, skip=skip, limit=limit)
    return spCapaQuotDeps


@app.post("/db/create_spCapaQuotDep", response_model=schemas.SpCapaQuotDep)
def create_spCapaQuotDep(spCapaQuotDepCreate: schemas.SpCapaQuotDepCreate, db: Session = Depends(get_db)):
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
def create_flashFra(flashFraCreate: schemas.FlashFraCreate, db: Session = Depends(get_db)):
    flashFra = crud.create_flashFra(db, flashFra=flashFraCreate)
    return flashFra


@app.get("/db/getRowNumber_flashFra")
def rowNumber_flashFra(db: Session = Depends(get_db)):
    rows = db.query(models.FlashFra).count()
    return rows
