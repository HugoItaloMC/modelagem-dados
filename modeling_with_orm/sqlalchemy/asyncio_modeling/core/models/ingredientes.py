import json

from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List, Iterable

from utils.model_base import Base
from utils.helper import data_para_string
from models.weak_tables import IngredientesPicoles


class Ingredientes(Base):

    __tablename__: str = "ingredientes"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, nullable=False)

    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True, nullable=False)

    name: Mapped[str] = mapped_column(String(45), unique=True, nullable=True)

    picole: Mapped[List['Picoles']] = relationship(secondary='ingredientes_picoles', back_populates='ingredientes',
                                                   lazy='joined', viewonly=True)

    picole_association: Mapped[List['IngredientesPicoles']] = relationship(back_populates='ingredientes')

    def __iter__(self):
        yield from {
            "ID": "%d" % int(self.id),
            "name": "%s" % self.name,
            "date_create": "%s\n" % data_para_string(self.date_create)
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()