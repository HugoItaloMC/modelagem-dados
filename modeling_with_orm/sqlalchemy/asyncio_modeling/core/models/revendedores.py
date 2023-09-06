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

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys() if not attr.startswith("_sa_instance_state")})}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
