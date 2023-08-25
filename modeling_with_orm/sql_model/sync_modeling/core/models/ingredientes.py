from sqlmodel import SQLModel, Field

import json
from datetime import datetime
from typing import Optional, Iterable, Generator

from utils.helper import data_para_string



class Ingredientes(SQLModel, table=True):

    __tablename__: str = "ingredientes"

    id: Optional[int] = Field(primary_key=True, default=None)

    date_create: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(max_length=45, unique=True)

    def __iter__(self):
        yield from {
            "ID": "%d" % int(self.id),
            "name": "%s" % self.nome,
            "date_create": "%s\n" % data_para_string(self.date_create)
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()