from sqlmodel import SQLModel, Relationship, Field

import json
from datetime import datetime
from typing import Iterable, Optional, List


from utils.helper import data_para_string
from models.tipo_picole import TiposPicole
from models.weak_tables import LotesNotasFiscais


class Lotes(SQLModel, table=True):

    __tablename__: str = "lotes"

    id: Optional[int] = Field(primary_key=True, default=None)
    date_create: datetime = Field(default=datetime.now(), index=True)

    quantidade: int = Field(nullable=True)

    # Settings relationship
    id_tipos_picole: int = Field(default=None, foreign_key='tipos_picole.id')
    tipo_picole: TiposPicole = Relationship(sa_relationship_kwargs={'lazy': 'joined'})
    nota_fiscal: List['NotasFiscais'] = Relationship(link_model=LotesNotasFiscais, sa_relationship_kwargs={"lazy": "dynamic", "viewonly": True}, back_populates='lote')

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%d" % self.id,
            "quantidade": "%d" % self.quantidade,
            "id_tipos_picole": "%d" % self.id_tipos_picole,
            "tipos_picole": "%s" % " ".join(map(str, self.tipo_picole))}.items()

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
