from sqlmodel import SQLModel, Field

from datetime import datetime
import json
from typing import Iterable, Optional


class TiposEmbalagem(SQLModel, table=True):

    __tablename__: str = "tipos_embalagem"

    id: Optional[int] = Field(primary_key=True, default=None)
    date_create: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(max_length=45)

    # Settings to relationship's
    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "tipo_embalagem": "%s" % self.nome,
        }.items()

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

