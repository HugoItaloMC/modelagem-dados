
from sqlalchemy import Integer, BigInteger, DateTime, DECIMAL, ForeignKey, Column
from sqlalchemy.orm import relationship
from datetime import datetime

import json
from typing import Iterable, List, Optional

from utils.model_base import Base
from models.weak_tables import (aditivo_nutritivo_picole, ingredientes_picoles, conservantes_picoles)

from models.ingredientes import Ingredientes
from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivoNutritivo
from models.sabores import Sabores
from models.tipo_picole import TiposPicole
from models.tipos_embalagem import TiposEmbalagem


class Picoles(Base):

    __tablename__: str = "picoles"
    Column('id', BigInteger, autoincrement=True, nullable=False),
    Column('preco', DECIMAL(8, 2), nullable=False)

    # ForeignKey's
    Column('id_sabor', BigInteger, ForeignKey('sabores.id'), nullable=False),
    sabor = relationship('Sabores', lazy='joined'),

    Column('id_tipo_embalagem', BigInteger, ForeignKey('tipos_embalagem.id'), nullable=False)
    tipos_embalagem = relationship('TiposEmbalagem', lazy='joined')

    Column('id_tipo_picole', BigInteger, ForeignKey('tipos_picole.id'), nullable=True)
    tipos_picole = relationship('TiposPicole', lazy='joined')

    # Complex relation
    ingrediente: List[Ingredientes] = relationship('Ingrediente',
                                                   secondary=ingredientes_picoles,
                                                   backref='ingredientes')

    conservantes: List[Conservantes] = relationship('Conservantes',
                                                    secondary=conservantes_picoles,
                                                    backref='conservantes')

    aditivo_nutritivo: List[AditivoNutritivo] = relationship('AditivoNutritivo',
                                                             secondary=aditivo_nutritivo_picole,
                                                             backref='aditivo_nutritivo')

    def __iter__(self) -> Iterable:
        yield from {
            "date_create": "%s" % self.date_create, "id": "%d" % int(self.id), "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social, "contato": "%s" % self.contato}.items()

    def __str__(self):
        # Is String object from json
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        #  Whas is str
        return self.__str__()
