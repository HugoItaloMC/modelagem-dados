from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import json
from datetime import datetime

from utils.model_base import Base
from utils.helper import data_para_string


class AditivoNutritivo(Base):

    __tablename__: str = 'aditivos_nutritivos'
    id: Mapped[int] = mapped_column('id', BigInteger, primary_key=True, autoincrement=True, nullable=False)

    date_create: Mapped[datetime] = mapped_column('date_create', DateTime, default=datetime.now, index=True, nullable=False)

    nome: Mapped[str] = mapped_column('nome', String(45), nullable=False)

    formula_quimica: Mapped[str] = mapped_column('formula_quimica', String(200), nullable=False)

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys() if not attr.startswith("_sa_instance_state")})}.items()

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
