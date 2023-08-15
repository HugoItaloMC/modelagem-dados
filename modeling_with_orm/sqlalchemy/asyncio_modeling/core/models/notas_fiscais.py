from sqlalchemy import String, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
import json
from typing import Iterable, List, Generator

from utils.model_base import Base
from utils.helper import data_para_string
from models.revendedores import Revendedores
from models.lotes import Lotes


class NotasFiscais(Base):

    __tablename__: str = "notas_fiscais"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True)

    valor = mapped_column(DECIMAL(8, 2), nullable=False)

    numero_serie: Mapped[str] = mapped_column(String(45), nullable=False)

    descricao: Mapped[str] = mapped_column(String(200), nullable=False)
    # Settings to relationship
    id_revendedor: Mapped[int] = mapped_column(BigInteger, ForeignKey('revendedores.id'))

    revendedor: Mapped['Revendedores'] = relationship('Revendedores', backref='revendedores', lazy='joined')

    lote: Mapped[List['Lotes']] = relationship(secondary='lotes_notas_fiscais', back_populates='notas_fiscais',
                                               lazy='dynamic', viewonly=True)

    lote_association: Mapped[List['LotesNotasFiscais']] = relationship(back_populates='nota_fiscal')

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
