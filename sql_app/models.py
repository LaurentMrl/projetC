from sqlalchemy import Column, Integer, String, Date, Float

from database import Base


class SpPosQuotDep(Base):
    __tablename__ = "sp_pos_quot_dep"

    id = Column(Integer, primary_key=True, index=True)
    dep = Column(Integer, index=True)
    jour = Column(Date, index=True)
    P = Column(Integer, index=True)
    T = Column(Integer, index=True)
    cl_age90 = Column(Integer, index=True)
    pop = Column(Integer, index=True)


class SpPosQuotFra(Base):
    __tablename__ = "sp_pos_quot_fra"

    id = Column(Integer, primary_key=True, index=True)
    fra = Column(String, index=True)
    jour = Column(Date, index=True)
    P_f = Column(Integer, index=True)
    P_h = Column(Integer, index=True)
    P = Column(Integer, index=True)
    T_f = Column(Integer, index=True)
    T_h = Column(Integer, index=True)
    T = Column(Integer, index=True)
    cl_age90 = Column(Integer, index=True)
    pop = Column(Integer, index=True)


class SpPeTbQuotFra(Base):
    __tablename__ = "sp_pe_tb_quot_fra"

    id = Column(Integer, primary_key=True, index=True)
    fra = Column(String, index=True)
    jour = Column(Date, index=True)
    P_f = Column(Integer, index=True)
    P_h = Column(Integer, index=True)
    P = Column(Integer, index=True)
    pop_f = Column(Float, index=True)
    pop_h = Column(Float, index=True)
    cl_age90 = Column(Integer, index=True)
    pop = Column(Float, index=True)


class SpPeTbQuotDep(Base):
    __tablename__ = "sp_pe_tb_quot_dep"

    id = Column(Integer, primary_key=True, index=True)
    dep = Column(Integer, index=True)
    jour = Column(Date, index=True)
    P = Column(Integer, index=True)
    cl_age90 = Column(Integer, index=True)
    pop = Column(Integer, index=True)


class SpCapaQuotFra(Base):
    __tablename__ = "sp_capa_quot_fra"

    id = Column(Integer, primary_key=True, index=True)
    fra = Column(String, index=True)
    jour = Column(Date, index=True)
    pop = Column(Integer, index=True)
    T = Column(Integer, index=True)


class SpCapaQuotDep(Base):
    __tablename__ = "sp_capa_quot_dep"

    id = Column(Integer, primary_key=True, index=True)
    dep = Column(Integer, index=True)
    jour = Column(Date, index=True)
    pop = Column(Integer, index=True)
    T = Column(Integer, index=True)


class FlashFra(Base):
    __tablename__ = "flash_fra"

    id = Column(Integer, primary_key=True, index=True)
    fra = Column(String, index=True)
    deb_periode = Column(Date, index=True)
    flash_variants = Column(Integer, index=True)
    n = Column(Integer, index=True)
    n_tot = Column(Integer, index=True)
