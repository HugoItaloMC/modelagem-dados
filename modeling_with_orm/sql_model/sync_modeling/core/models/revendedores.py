from sqlmodel import SQLModel, Field

from datetime import datetime
from typing import List
import json
from typing import Iterable, Generator, Optional

from utils.helper import data_para_string


class Revendedores(SQLModel, table=True):

    __tablename__: str = "revendedores"

    id: int = Field(primary_key=True, default=None)

    date_create: datetime = Field(default=datetime.now(), index=True)

    cnpj: str = Field(max_length=45, unique=True, nullable=False)

    razao_social: str = Field(max_length=100, unique=True, nullable=False)

    contato: str = Field(max_length=45, unique=True, nullable=False)

    def __iter__(self) -> Iterable[Generator]:
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%d" % int(self.id),
            "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social,
            "contato": "%s" % self.contato
        }.items()

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

