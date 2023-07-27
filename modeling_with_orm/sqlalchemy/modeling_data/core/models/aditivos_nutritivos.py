import json

from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from utils.model_base import Base


class AditivoNutritivo(Base):

    __tablename__: str = "aditivo_nutritivo"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    name: Mapped[str] = mapped_column(String(45),
                                      unique=True,
                                      nullable=True)

    formula: Mapped[str] = mapped_column(String(200),
                                         unique=True,
                                         nullable=True)

    def __iter__(self) -> dict:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "name": "%s" % self.name,
            "formula": "%s" % self.formula
        }

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
