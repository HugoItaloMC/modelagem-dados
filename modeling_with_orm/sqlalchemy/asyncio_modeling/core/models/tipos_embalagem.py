
from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
import json
from typing import Iterable, List

from utils.model_base import Base


class TiposEmbalagem(Base):

    __tablename__: str = "tipos_embalagem"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    name: Mapped[str] = mapped_column(String(45),
                                       unique=True,
                                       nullable=True)

    # Settings to relationship's
    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "tipo_embalagem": "%s" % self.name,
        }

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()

