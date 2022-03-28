from datetime import date

from pydantic import BaseModel


class SpPosQuotDepBase(BaseModel):
    dep: int
    jour: date
    P: int
    T: int
    cl_age90: int
    pop: int


class SpPosQuotDepCreate(SpPosQuotDepBase):
    pass


class SpPosQuotDep(SpPosQuotDepBase):
    id: int

    class Config:
        orm_mode = True


class SpPeTbQuotFraBase(BaseModel):
    fra: str
    jour: date
    P_f: int
    P_h: int
    P: int
    pop_f: float
    pop_h: float
    cl_age90: int
    pop: float


class SpPeTbQuotFraCreate(SpPeTbQuotFraBase):
    pass


class SpPeTbQuotFra(SpPeTbQuotFraBase):
    id: int

    class Config:
        orm_mode = True


class SpPeTbQuotDepBase(BaseModel):
    dep: int
    jour: date
    P: int
    cl_age90: int
    pop: int


class SpPeTbQuotDepCreate(SpPeTbQuotDepBase):
    pass


class SpPeTbQuotDep(SpPeTbQuotDepBase):
    id: int

    class Config:
        orm_mode = True


class SpCapaQuotFraBase(BaseModel):
    fra: int
    jour: date
    pop: int
    T: int


class SpCapaQuotFraCreate(SpCapaQuotFraBase):
    pass


class SpCapaQuotFra(SpCapaQuotFraBase):
    id: int

    class Config:
        orm_mode = True


class SpCapaQuotDepBase(BaseModel):
    dep: int
    jour: date
    pop: int
    T: int


class SpCapaQuotDepCreate(SpCapaQuotDepBase):
    pass


class SpCapaQuotDep(SpCapaQuotDepBase):
    id: int

    class Config:
        orm_mode = True


class FlashFraBase(BaseModel):
    fra: int
    deb_periode: date
    flash_variants: int
    n: int
    n_tot: int


class FlashFraCreate(FlashFraBase):
    pass


class FlashFra(FlashFraBase):
    id: int

    class Config:
        orm_mode = True
