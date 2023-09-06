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

    quantidade: Mapped[int] = mapped_column("quantidade", BigInteger, nullable=False)

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys() if not attr.startswith("_sa_instance_state")})}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=4)

    def __repr__(self):
        return self.__str__()
