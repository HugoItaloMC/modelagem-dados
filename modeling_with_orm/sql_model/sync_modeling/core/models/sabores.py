from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint

import json
from datetime import datetime
from typing import Optional, Iterable, Generator

from utils.helper import data_para_string


class Sabores(SQLModel, table=True):

    __tablename__: str = "sabores"

    id: Optional[int] = Field(primary_key=True, default=None)
    date_create: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(unique=True, nullable=False)

    def __iter__(self) -> Iterable[Generator]:
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%d" % int(self.id),
            "sabor": "%s" % self.sabor,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
