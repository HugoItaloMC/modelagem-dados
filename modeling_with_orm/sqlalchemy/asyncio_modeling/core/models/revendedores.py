from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List
import json
from typing import Iterable, Generator

from utils.model_base import Base
from utils.helper import data_para_string


class Revendedores(Base):

    __tablename__: str = "revendedores"

    id: Mapped[int] = mapped_column("id", BigInteger, primary_key=True, autoincrement=True, nullable=False)

    date_create: Mapped[datetime] = mapped_column("date_create", DateTime, default=datetime.today,
                                                  nullable=False, index=True)

    cnpj: Mapped[str] = mapped_column("cnpj", String(45), nullable=False)

    razao_social: Mapped[str] = mapped_column("razao_social", String(100), nullable=False)

    contato: Mapped[str] = mapped_column("contato", String(45), nullable=False)

    def __iter__(self) -> Iterable:
        yield from {
            "data_criaca": "%s" % data_para_string(self.date_create),
            "id": "%d" % self.id,
            "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social,
            "contato": "%s" % self.contato
        }.items()

    def __str__(self) -> str:
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
