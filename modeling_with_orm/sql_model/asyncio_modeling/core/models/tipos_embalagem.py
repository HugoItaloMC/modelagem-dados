
from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
import json
from typing import Iterable, List

from utils.model_base import Base
from utils.helper import data_para_string

class TiposEmbalagem(Base):

    __tablename__: str = 'tipos_embalagem'

    id: Mapped[int] = mapped_column('id', BigInteger, primary_key=True, autoincrement=True, nullable=False)

    data_create: Mapped[datetime] = mapped_column('date_create', DateTime, default=datetime.now, index=True)

    nome: Mapped[str] = mapped_column('nome', String(45), nullable=False)

    def __iter__(self) -> Iterable:
        yield from {
            "data_criacao": "%s" % data_para_string(self.data_create),
            "id": "%d" % self.id,
            "nome": "%s" % self.nome
        }.items()

    def __str__(self) -> str:
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
