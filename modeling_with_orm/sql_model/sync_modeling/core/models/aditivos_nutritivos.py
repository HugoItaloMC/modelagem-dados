from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint
import json
from datetime import datetime
from typing import Optional, List

from utils.helper import data_para_string


class AditivoNutritivo(SQLModel, table=True):

    __tablename__: str = "aditivos_nutritivos"

    id: Optional[int] = Field(primary_key=True, default=None)
    date_create: datetime = Field(default=datetime.now(), index=True)

    nome: str = Field(max_length=45)
    formula_quimica: str = Field(max_length=100)

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
