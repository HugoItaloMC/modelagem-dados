from sqlalchemy import Integer, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

import json
from typing import Iterable, List, Optional

from utils.model_base import Base
from models.weak_tables import (AditivoNutritivoPicoles, IngredientesPicoles, ConservantesPicoles)

from models.ingredientes import Ingredientes
from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivoNutritivo
from models.sabores import Sabores
from models.tipo_picole import TiposPicole
from models.tipos_embalagem import TiposEmbalagem


class Picoles(Base):

    __tablename__: str = "picoles"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, unique=True)

    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, index=True)

    valor = mapped_column(DECIMAL(8, 2), nullable=False)

    # Settings to relationship's >>
    # Relation `Sabores`
    id_sabor: Mapped[int] = mapped_column(BigInteger, ForeignKey('sabores.id'), nullable=False, primary_key=True)

    sabor: Mapped['Sabores'] = relationship('Sabores', lazy='joined')

    # Relation `TiposEmbalagem`
    id_tipo_embalagem: Mapped[int] = mapped_column(BigInteger, ForeignKey('tipos_embalagem.id'), nullable=False, primary_key=True)

    tipos_embalagem: Mapped['TiposEmbalagem'] = relationship('TiposEmbalagem', lazy='joined')

    # Relation `TiposPicole`
    id_tipos_picole: Mapped[int] = mapped_column(BigInteger, ForeignKey('tipos_picole.id'), nullable=False)

    tipos_picole: Mapped['TiposPicole'] = relationship('TiposPicole', lazy='joined')
    # Settings Weak Tables

    # Weak `ingredientes_picoles`
    ingredientes: Mapped[List['Ingredientes']] = relationship('Ingredientes', secondary='ingredientes_picoles',
                                                            back_populates='picole', lazy='joined', viewonly=True)

    ingredientes_association: Mapped[List['IngredientesPicoles']] = relationship('IngredientesPicoles', back_populates='picole')

    #  Weak `conservantes_picoles`
    conservantes: Mapped[Optional[List['Conservantes']]] = relationship('Conservantes', secondary='conservantes_picoles',
                                                            back_populates='picole',lazy='joined', viewonly=True)

    conservantes_association: Mapped[List['ConservantesPicoles']] = relationship('ConservantesPicoles', back_populates='picole')

    # # Weak `aditivos_nutritivos`
    aditivos_nutritivos: Mapped[Optional[List['AditivoNutritivo']]] = relationship('AditivoNutritivo',
                                                                       secondary='aditivo_nutritivo_picole',
                                                                       back_populates='picole', lazy='joined',
                                                                       viewonly=True)

    aditivo_nutritivo_association: Mapped[List['AditivoNutritivoPicoles']] = relationship('AditivoNutritivoPicoles', back_populates='picole')

    def __iter__(self) -> Iterable:
        # For object generator type iterable
        yield from {
            "date_create": "%s" % self.date_create, "id": "%d" % int(self.id), "cnpj": "%s" % self.cnpj,
            "razao_social": "%s" % self.razao_social, "contato": "%s" % self.contato}

    def __str__(self) -> str:
        # Is String object from json
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self) -> str:
        #  Whas is str
        return self.__str__()
