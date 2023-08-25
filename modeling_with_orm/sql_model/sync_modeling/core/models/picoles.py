from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

import json
from typing import Iterable, List, Optional


from models.weak_tables import (AditivoNutritivoPicoles, IngredientesPicoles, ConservantesPicoles)

from models.ingredientes import Ingredientes
from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivoNutritivo
from models.sabores import Sabores
from models.tipo_picole import TiposPicole
from models.tipos_embalagem import TiposEmbalagem


class Picoles(SQLModel, table=True):

    __tablename__: str = "picoles"

    id: Optional[int] = Field(default=None, primary_key=True)
    date_create: datetime = Field(default=datetime.now(), index=True)
    preco: float = Field()

    # ForeignKey's
    id_sabor: Optional[int] = Field(default=None, foreign_key='sabores.id')
    sabor: Sabores = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "delete"})

    id_tipo_embalagem: Optional[int] = Field(default=None, foreign_key='tipos_embalagem.id')
    tipos_embalagem: TiposEmbalagem = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "delete"})

    id_tipos_picole: Optional[int] = Field(default=None, foreign_key='tipos_picole.id')
    tipos_picole: TiposPicole = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "delete"})

    # Complex relation
    ingrediente: Ingredientes = Relationship(link_model=IngredientesPicoles, sa_relationship_kwargs={"lazy": "joined",
                                                                                                    "viewonly": True})

    conservantes: Conservantes = Relationship(link_model=ConservantesPicoles, sa_relationship_kwargs={"lazy": "joined",
                                                                                                     "viewonly": True})

    aditivo_nutritivo: AditivoNutritivo = Relationship(link_model=AditivoNutritivoPicoles,
                                                       sa_relationship_kwargs={"lazy": "joined", "viewonly": True})

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create, "id": "%d" % int(self.id), "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social, "contato": "%s" % self.contato}.items()

    def __str__(self):
        # Is String object from json
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        #  Whas is str
        return self.__str__()
