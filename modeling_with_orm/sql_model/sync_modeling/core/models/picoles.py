from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

import json
from typing import Iterable, Generator, Optional, List


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
    sabor: List[Sabores] = Relationship(sa_relationship_kwargs={"lazy": "joined", "viewonly": True})

    id_tipo_embalagem: Optional[int] = Field(default=None, foreign_key='tipos_embalagem.id')
    tipos_embalagem: List[TiposEmbalagem] = Relationship(sa_relationship_kwargs={"lazy": "joined", "viewonly": True})

    id_tipos_picole: Optional[int] = Field(default=None, foreign_key='tipos_picole.id')
    tipos_picole: List[TiposPicole] = Relationship(sa_relationship_kwargs={"lazy": "joined", "viewonly": True})

    # Complex relation
    ingrediente: List[Ingredientes] = Relationship(link_model=IngredientesPicoles, sa_relationship_kwargs={"lazy": "joined",
                                                                                                           "viewonly": True})

    conservantes: List[Conservantes] = Relationship(link_model=ConservantesPicoles, sa_relationship_kwargs={"lazy": "joined",
                                                                                                            "viewonly": True})

    aditivo_nutritivo: List[AditivoNutritivo] = Relationship(link_model=AditivoNutritivoPicoles,
                                                             sa_relationship_kwargs={"lazy": "joined", "viewonly": True})

    # Abaixo Representacão do Objeto
    def __iter__(self) -> Iterable[Generator]:
        yield from {"date_create": "%s" % self.date_create,
                    "id": "%d" % self.id,
                    "preco": "%.2f" % self.preco,
                    "id_sabor": "%d" % self.id_sabor,
                    "sabor": "%s" % " ".join(map(str, self.sabor)),
                    "id_tipo_embalagem": "%d" % self.id_tipo_embalagem,
                    "tipo_embalagem": "%s" % " ".join(map(str, self.tipos_embalagem)),
                    "id_tipo_picole": "%d" % self.id_tipos_picole,
                    "tipo_picole": "%s" % " ".join(map(str, self.tipos_picole))}.items()

    def __str__(self):
        # Is String object from json
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        #  Whas is str
        return self.__str__()
