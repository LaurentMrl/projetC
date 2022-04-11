from sqlalchemy.orm import Session

from . import models, schemas


def get_spPosQuotDep(db: Session, spPosQuotDep_id: int):
    return db.query(models.SpPosQuotDep).filter(models.SpPosQuotDep.id == spPosQuotDep_id).first()


def get_spPosQuotDeps(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.SpPosQuotDep).offset(skip).limit(limit).all()


def create_spPosQuotDep(db: Session, spPosQuotDep: schemas.SpPosQuotDepCreate):
    db_spPosQuotDep = models.SpPosQuotDep(dep=spPosQuotDep.dep, jour=spPosQuotDep.jour, P=spPosQuotDep.P,
                                          T=spPosQuotDep.T, cl_age90=spPosQuotDep.cl_age90, pop=spPosQuotDep.pop)
    db.add(db_spPosQuotDep)
    db.commit()
    db.refresh(db_spPosQuotDep)
    return db_spPosQuotDep


def get_spPeTbQuotFra(db: Session, spPeTbQuotFra_id: int):
    return db.query(models.SpPeTbQuotFra).filter(models.SpPeTbQuotFra.id == spPeTbQuotFra_id).first()


def get_spPeTbQuotFras(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.SpPeTbQuotFra).offset(skip).limit(limit).all()


def create_spPeTbQuotFra(db: Session, spPeTbQuotFra: schemas.SpPeTbQuotFraCreate):
    db_spPeTbQuotFra = models.SpPeTbQuotFra(fra=spPeTbQuotFra.fra, jour=spPeTbQuotFra.jour, P_f=spPeTbQuotFra.P_f,
                                            P_h=spPeTbQuotFra.P_h, P=spPeTbQuotFra.P, pop_f=spPeTbQuotFra.pop_f,
                                            pop_h=spPeTbQuotFra.pop_h, cla_age90=spPeTbQuotFra.cl_age90,
                                            pop=spPeTbQuotFra.pop)
    db.add(db_spPeTbQuotFra)
    db.commit()
    db.refresh(db_spPeTbQuotFra)
    return db_spPeTbQuotFra


def get_spPeTbQuotDep(db: Session, spPeTbQuotDep_id: int):
    return db.query(models.SpPeTbQuotDep).filter(models.SpPeTbQuotDep.id == spPeTbQuotDep_id).first()


def get_spPeTbQuotDeps(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.SpPeTbQuotDep).offset(skip).limit(limit).all()


def create_spPeTbQuotDep(db: Session, spPeTbQuotDep: schemas.SpPeTbQuotDepCreate):
    db_spPeTbQuotDep = models.SpPeTbQuotDep(dep=spPeTbQuotDep.dep, jour=spPeTbQuotDep.jour, P=spPeTbQuotDep.P,
                                            cl_age90=spPeTbQuotDep.cl_age90, pop=spPeTbQuotDep.pop)
    db.add(db_spPeTbQuotDep)
    db.commit()
    db.refresh(db_spPeTbQuotDep)
    return db_spPeTbQuotDep


def get_spCapaQuotFra(db: Session, spCapaQuotFra_id: int):
    return db.query(models.SpCapaQuotFra).filter(models.SpCapaQuotFra.id == spCapaQuotFra_id).first()


def get_spCapaQuotFras(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.SpCapaQuotFra).offset(skip).limit(limit).all()


def create_spCapaQuotFra(db: Session, spCapaQuotFra: schemas.SpCapaQuotFraCreate):
    db_spCapaQuotFra = models.SpCapaQuotFra(fra=spCapaQuotFra.fra, jour=spCapaQuotFra.jour, pop=spCapaQuotFra.pop,
                                            T=spCapaQuotFra.T)
    db.add(db_spCapaQuotFra)
    db.commit()
    db.refresh(db_spCapaQuotFra)
    return db_spCapaQuotFra


def get_spCapaQuotDep(db: Session, spCapaQuotDep_id: int):
    return db.query(models.SpCapaQuotDep).filter(models.SpCapaQuotDep.id == spCapaQuotDep_id).first()


def get_spCapaQuotDeps(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.SpCapaQuotDep).offset(skip).limit(limit).all()


def create_spCapaQuotDep(db: Session, spCapaQuotDep: schemas.SpCapaQuotDepCreate):
    db_spCapaQuotDep = models.SpCapaQuotDep(dep=spCapaQuotDep.dep, jour=spCapaQuotDep.jour, pop=spCapaQuotDep.pop,
                                            T=spCapaQuotDep.T)
    db.add(db_spCapaQuotDep)
    db.commit()
    db.refresh(db_spCapaQuotDep)
    return db_spCapaQuotDep


def get_flashFra(db: Session, flashFra_id: int):
    return db.query(models.FlashFra).filter(models.FlashFra.id == flashFra_id).first()


def get_flashFras(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.FlashFra).offset(skip).limit(limit).all()


def create_flashFra(db: Session, flashFra: schemas.FlashFraCreate):
    db_flashFra = models.FlashFra(fra=flashFra.fra, deb_periode=flashFra.deb_periode,
                                  flash_variants=flashFra.flash_variants, n=flashFra.n, n_tot=flashFra.n_tot)
    db.add(db_flashFra)
    db.commit()
    db.refresh(db_flashFra)
    return db_flashFra
