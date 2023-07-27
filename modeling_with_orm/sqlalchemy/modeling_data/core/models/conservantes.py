from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column

import json
from datetime import datetime
from typing import Iterable, Any

from utils.model_base import Base


class Conservantes(Base):

    __tablename__: str = "conservantes"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    name: Mapped[str] = mapped_column(String(45),
                                      unique=True,
                                      nullable=True)

    descricao: Mapped[str] = mapped_column(String(200),
                                           nullable=True)

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "conservantes": "%s" % self.name,
            "descricao": "%s" % self.descricao
        }

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

