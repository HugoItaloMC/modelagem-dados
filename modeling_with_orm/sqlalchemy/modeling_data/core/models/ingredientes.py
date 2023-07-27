from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from utils.model_base import Base


class Ingredientes(Base):

    __tablename__: str = "ingredientes"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    name: Mapped[str] = mapped_column(String(45),
                                      unique=True,
                                      nullable=True)

    def __repr__(self) -> dict:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "ingredientes": "%s" % self.name,
        }
