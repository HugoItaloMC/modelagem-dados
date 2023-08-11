
from sqlalchemy import Integer, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

import json
from typing import Iterable, List, Generator

from utils.model_base import Base
from utils.helper import data_para_string
from models.tipo_picole import TiposPicole


class Lotes(Base):

    __tablename__: str = "lotes"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True)

    quantidade: Mapped[str] = mapped_column(Integer, nullable=True)
    # Settings relationship
    id_tipos_picole: Mapped[int] = mapped_column(BigInteger, ForeignKey('tipos_picole.id'))

    tipo_picole: Mapped['TiposPicole'] = relationship('TiposPicole', lazy='joined')

    notas_fiscais: Mapped[List['NotasFiscais']] = relationship(secondary='lotes_notas_fiscais', back_populates='lote',
                                                               lazy='joined', viewonly=True)

    nota_fiscal_association: Mapped[List['LotesNotasFiscais']] = relationship(back_populates='lote')

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%d" % int(self.id),
            "quantidade": "%s" % self.cnpj,
            "id_tipos_picole": "%d" % int(self.id_tipos_picole)
        }.items()

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
