from sqlmodel import SQLModel, Field

import json
from datetime import datetime
from typing import Iterable, Optional

from utils.helper import data_para_string


class Conservantes(SQLModel, table=True):

    __tablename__: str = "conservantes"

    id: Optional[int] = Field(primary_key=True, default=None)

    date_create: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(max_length=45, unique=True)

    descricao: str = Field(max_length=100, nullable=True)

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%d" % int(self.id),
            "conservantes": "%s" % self.nome,
            "descricao": "%s\n" % self.descricao
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
