from sqlalchemy import Integer, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

import json
from typing import Iterable

from utils.model_base import Base
from utils.helper import data_para_string
from models.tipo_picole import TiposPicole


class Lotes(Base):

    __tablename__: str = 'lotes'

    id: Mapped[int] = mapped_column('id', BigInteger, primary_key=True, autoincrement=True, unique=True)

    id_tipos_picole: Mapped[int] = mapped_column('id_tipos_picole', Integer,
                                                 ForeignKey('tipos_picole.id',
                                                            ondelete="CASCADE",
                                                            name='fk_tipos_picole_id'),
                                                 primary_key=True, nullable=False)

    tipos_picole: Mapped[TiposPicole] = relationship('TiposPicole', backref='tipos_picole',
                                                       lazy='joined',
                                                       cascade='delete')

    date_create: Mapped[datetime] = mapped_column('date_create', default=datetime.now, index=True)

    quantidade: Mapped[int] = mapped_column('quantidade', Integer, nullable=False)

    def __iter__(self) -> Iterable:
        yield from {
            "data_criacao": "%s" % data_para_string(self.date_create),
            "id": "%d" % self.id,
            "quantidade": "%d" % self.quantidade
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
