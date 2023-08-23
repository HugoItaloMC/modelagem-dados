from sqlmodel import SQLModel, Field

import json
from datetime import datetime
from typing import Generator, Iterable, Optional


class TiposPicole(SQLModel, table=True):

    __tablename__: str = "tipos_picole"

    id: Optional[int] = Field(primary_key=True, default=None)

    date_create: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(max_length=45, unique=True)

    def __iter__(self) -> Iterable[Generator]:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "tipo_picole": "%s" % self.nome,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
