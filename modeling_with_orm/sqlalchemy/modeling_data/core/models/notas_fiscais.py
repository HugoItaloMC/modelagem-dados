
from sqlalchemy import String, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
import json
from typing import Iterable

from utils.model_base import Base
from models.revendedores import Revendedores

class NotasFiscais(Base):

    __tablename__: str = "notas_fiscais"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    valor: Mapped[str] = mapped_column(DECIMAL(8, 2),
                                      unique=True,
                                      nullable=True)

    numero_serie: Mapped[str] = mapped_column(String(45),
                                              unique=True,
                                              nullable=False)

    descricao: Mapped[str] = mapped_column(String(200),
                                         nullable=True)
    # Settings to relationship
    id_revendedor: Mapped[int] = mapped_column(BigInteger,
                                               ForeignKey('revendedores.id'))

    revendedor: Mapped['Revendedores'] = relationship('Revendedores',
                                                      lazy='joined')

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social,
            "contato": "%s" % self.contato
        }

    def __str__(self):
        return json.dumps(dict(self),
                          ensure_ascii=False)

    def __repr__(self) -> str:
        return self.__str__()
