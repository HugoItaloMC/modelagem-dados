import json

from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import Generator, Iterable, List

from utils.model_base import Base
from utils.helper import data_para_string


class TiposPicole(Base):

    __tablename__: str = 'tipos_picole'

    id: Mapped[int] = mapped_column('id', BigInteger, autoincrement=True, primary_key=True, nullable=False)

    date_create: Mapped[datetime] = mapped_column('date_create', DateTime, default=datetime.now,
                                                  nullable=False, index=True)

    nome: Mapped[str] = mapped_column('nome', String(45), nullable=False)

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys() if
                                   not attr.startswith("_sa_instance_state")})}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
