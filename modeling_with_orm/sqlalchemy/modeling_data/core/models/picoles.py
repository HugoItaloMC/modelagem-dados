
from sqlalchemy import Integer, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

import json
from typing import Iterable, List

from utils.model_base import Base
from models.weak_tables import (ingredientes_picoles,
                         aditivos_nutritivos_picole,
                         conservantes_picoles)

from models.ingredientes import Ingredientes
from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivoNutritivo
from models.sabores import Sabores
from models.tipo_picole import TiposPicole
from models.tipos_embalagem import TiposEmbalagem


class Picoles(Base):

    __tablename__: str = "picoles"

    id: Mapped[int] = mapped_column(BigInteger,
                                    primary_key=True,
                                    autoincrement=True)

    date_create: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now,
                                                  index=True)

    valor: Mapped[str] = mapped_column(DECIMAL(8, 2),
                                      unique=True,
                                      nullable=False)

    # Settings to relationship's

    # Relation `Sabores`
    id_sabor: Mapped[int] = mapped_column(Integer,
                                          ForeignKey('sabores.id'),
                                          nullable=False)

    sabor: Mapped['Sabores'] = relationship('Sabores',
                                          lazy='joined')

    # Relation `TiposEmbalagem`
    id_tipo_embalagem: Mapped[int] = mapped_column(BigInteger,
                                                   ForeignKey('tipos_embalagem.id'), nullable=False)

    tipos_embalagem: Mapped['TiposEmbalagem'] = relationship('TiposEmbalagem', lazy='joined')

    # Relation `TiposPicole`
    id_tipos_picole: Mapped[int] = mapped_column(BigInteger,
                                                 ForeignKey('tipos_picole.id'), nullable=False)

    tipos_picole: Mapped['TiposPicole'] = relationship('TiposPicole', lazy='joined')
    # Settings Weak Tables

    # Weak `ingredientes_picoles`
    ingredientes: Mapped[List[Ingredientes]] = relationship('Ingredientes', secondary=ingredientes_picoles,
                                                            backref='ingredientes', lazy='joined')
    #  Weak `conservantes_picoles`
    conservantes: Mapped[List[Conservantes]] = relationship('Conservantes', secondary=conservantes_picoles,
                                                            backref='conservantes', lazy='joined')
    #  Weak `aditivos_nutritivos`
    aditivos_nutritivos: Mapped[List[AditivoNutritivo]] = relationship('AditivoNutritivo',
                                                                       secondary=aditivos_nutritivos_picole,
                                                                       backref='aditivos_nutritivos', lazy='joined')

    def __iter__(self) -> Iterable:
        # For object generator type iterable
        yield from {
            "date_create": "%s" % self.date_create,
            "id": "%d" % int(self.id),
            "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social,
            "contato": "%s" % self.contato
        }

    def __str__(self):
        # Is String object from json
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        #  Whas is str
        return self.__str__()
