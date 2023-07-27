
from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List
import json
from typing import Iterable

from utils.model_base import Base


class Revendedores(Base):

    __tablename__: str = "revendedores"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True, autoincrement=True, nullable=False)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now, index=True)

    cnpj: Mapped[str] = mapped_column(String(45),
                                      unique=True, nullable=False)

    razao_social: Mapped[str] = mapped_column(String(45),
                                              unique=True, nullable=False)

    contato: Mapped[str] = mapped_column(String(45),
                                         unique=True, nullable=False)

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social,
            "contato": "%s" % self.contato
        }

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

