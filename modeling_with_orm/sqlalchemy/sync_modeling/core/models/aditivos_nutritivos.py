from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import json
from datetime import datetime
from typing import Iterable, List

from utils.model_base import Base
from utils.helper import data_para_string
from models.weak_tables import AditivoNutritivoPicoles


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
    picole: Mapped[List['Picoles']] = relationship(secondary='aditivo_nutritivo_picole',
                                                   back_populates='aditivos_nutritivos', lazy='joined', viewonly=True)
    picole_association: Mapped[List['AditivoNutritivoPicoles']] = relationship(back_populates='aditivos_nutritivos')

    def __iter__(self):
        yield from {
            "date_create": "%s" % data_para_string(self.date_create),
            "id": "%s" % str(self.id),
            "name": "%s" % self.name,
            "formula": "%s\n" % self.formula
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    produto: AditivoNutritivo = AditivoNutritivo()
    produto.date_create: datetime = datetime.now()
    produto.name: str = 'sdlkfjslkd;fjsdklf'
    produto.formula: str = "jdfjksdfhsdljkfh"

    print(produto.__str__())
