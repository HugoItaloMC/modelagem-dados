
from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import json
from datetime import datetime
from typing import List

from utils.model_base import Base


class Sabores(Base):

    __tablename__: str = "sabores"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    sabor: Mapped[str] = mapped_column(String(45),
                                      unique=True,
                                       nullable=False)

    def __iter__(self) -> dict:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "sabor": "%s" % self.sabor,
        }

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False
                          )

    def __repr__(self):
        return self.__str__()
