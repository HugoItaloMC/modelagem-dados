from sqlmodel import SQLModel, Field, Relationship

from datetime import datetime
import json
from typing import Iterable, List, Generator, Optional

from utils.helper import data_para_string
from models.revendedores import Revendedores
from models.lotes import Lotes
from models.weak_tables import LotesNotasFiscais


class NotasFiscais(SQLModel, table=True):

    __tablename__: str = "notas_fiscais"

    id: Optional[int] = Field(primary_key=True, default=None)

    date_create: datetime = Field(default=datetime.now(), index=True)

    valor: float = Field(nullable=False)

    numero_serie: str = Field(max_length=45)

    descricao: str = Field(max_length=200, nullable=False)
    # Settings to relationship
    id_revendedor: Optional[int] = Field(foreign_key='revendedores.id')

    revendedor: Revendedores = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "delete"})

    lote: List[Lotes] = Relationship(link_model=LotesNotasFiscais, sa_relationship_kwargs={"lazy": "joined", "viewonly": True})



    def __iter__(self) -> Iterable[Generator]:
        yield from {"date_create": "%s" % data_para_string(self.date_create),
                    "id": "%d" % int(self.id),
                    "cnpj": "%s" % self.cnpj,
                    "razao_social": "%s" % self.razao_social,
                    "contato": "%s" % self.contato}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
