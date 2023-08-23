from sqlmodel import SQLModel, Relationship, Field

import json
from datetime import datetime
from typing import Iterable, Optional


from utils.helper import data_para_string
from models.tipo_picole import TiposPicole


class Lotes(SQLModel, table=True):

    __tablename__: str = "lotes"

    id: Optional[int] = Field(primary_key=True, default=None)
    date_create: datetime = Field(default=datetime.now(), index=True)

    quantidade: int = Field(nullable=True)

    # Settings relationship
    id_tipos_picole: int = Field(default=None, foreign_key='tipos_picole.id')
    tipo_picole: TiposPicole = Relationship(sa_relationship_kwargs={'lazy': 'joined'})

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%d" % int(self.id),
            "quantidade": "%s" % self.cnpj,
            "id_tipos_picole": "%d" % int(self.id_tipos_picole)
        }.items()

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
