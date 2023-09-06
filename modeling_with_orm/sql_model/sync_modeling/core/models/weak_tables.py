from sqlmodel import Field, SQLModel

from typing import Optional

# Weak Tables of `N=N` relations from `Picoles`


class AditivoNutritivoPicoles(SQLModel, table=True):
    #  N=N of `aditivos_nutritivos with picoles`

    __tablename__: str = 'aditivo_nutritivo_picole'
    id: Optional[int] = Field(default=None, primary_key=True)

    id_picole: Optional[int] = Field(default=None, foreign_key='picoles.id', index=True)
    id_aditivo_nutritivo: Optional[int] = Field(default=None, foreign_key='aditivos_nutritivos.id', index=True)


class IngredientesPicoles(SQLModel, table=True):
    #  N=N of `ingredientes with picoles`

    __tablename__: str = 'ingredientes_picoles'
    id: Optional[int] = Field(default=None, primary_key=True)

    id_picole: Optional[int] = Field(foreign_key='picoles.id', index=True)
    id_ingredientes: Optional[int] = Field(foreign_key='ingredientes.id', index=True)


class ConservantesPicoles(SQLModel, table=True):
    #  N=N of `ingredientes with picoles`

    __tablename__: str = 'conservantes_picoles'
    id: Optional[int] = Field(default=None, primary_key=True)

    id_picole: Optional[int] = Field(foreign_key='picoles.id')
    id_conservantes: Optional[int] = Field(foreign_key='conservantes.id')


class LotesNotasFiscais(SQLModel, table=True):
    # N=N of `notas_fiscais with lotes`

    __tablename__: str = 'lotes_notas_fiscais'

    id: int = Field(primary_key=True)

    id_lote: Optional[int] = Field(foreign_key='lotes.id')
    id_nota_fiscal: Optional[int] = Field(foreign_key='notas_fiscais.id')

