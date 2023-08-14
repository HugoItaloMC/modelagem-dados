import json

from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import Generator, Iterable, List

from utils.model_base import Base


class TiposPicole(Base):

    __tablename__: str = "tipos_picole"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, nullable=False)

    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True, nullable=False)

    name: Mapped[str] = mapped_column(String(45), unique=True, nullable=True)

    lote: Mapped[List['Lotes']] = relationship(secondary='lote_tipo_picole',
                                               back_populates='tipo_picole',
                                               lazy='joined',
                                               viewonly=True)

    lote_association: Mapped[List['LoteTipoPicole']] = relationship(back_populates='tipo_picole')

    # Settings to relationship's

    def __iter__(self) -> Iterable[Generator]:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "tipo_picole": "%s" % self.name,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
