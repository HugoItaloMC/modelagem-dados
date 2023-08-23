from sqlalchemy import Integer, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

import json
from typing import Iterable, List, Optional

from utils.model_base import Base

from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivoNutritivo
from models.ingredientes import Ingredientes
from models.sabores import Sabores
from models.tipo_picole import TiposPicole
from models.tipos_embalagem import TiposEmbalagem

from models.weak_tables import aditivo_nutritivo_picole, conservantes_picoles, ingredientes_picoles


class Picoles(Base):

    __tablename__: str = "picoles"

    id: Mapped[int] = mapped_column("id", BigInteger, primary_key=True,
                                    autoincrement=True, nullable=False, unique=False)

    date_create: Mapped[datetime] = mapped_column("date_create", DateTime,
                                                  default=datetime.today, nullable=False)

    preco: Mapped[float] = mapped_column('preco', DECIMAL(8, 2), nullable=False)

    id_sabor: Mapped[int] = mapped_column("id_sabor", BigInteger,
                                          ForeignKey('sabores.id',
                                                     name='fk_sabor_id',
                                                     ondelete="CASCADE"),
                                          nullable=False, index=True)

    sabor: Mapped[Sabores] = relationship('Sabores', lazy='joined', cascade='delete')

    id_tipos_embalagem: Mapped[int] = mapped_column("id_tipos_embalagem", BigInteger,
                                                    ForeignKey('tipos_embalagem.id',
                                                               name='fk_tipos_embalagem_id',
                                                               ondelete="CASCADE"),
                                                    nullable=False, index=True)

    tipos_embalagem: Mapped[TiposEmbalagem] = relationship("TiposEmbalagem", lazy='joined', cascade='delete')

    id_tipos_picole: Mapped[int] = mapped_column("id_tipos_picole", BigInteger,
                                                 ForeignKey("tipos_picole.id",
                                                            name='fk_tipos_picole_id',
                                                            ondelete="CASCADE"),
                                                 nullable=False, index=True)

    tipos_picole: Mapped[TiposPicole] = relationship("TiposPicole", lazy='joined', cascade='delete')

    ingrediente: Mapped[List[Ingredientes]] = relationship('Ingredientes', secondary=ingredientes_picoles,
                                                           backref='ingredientes', lazy='joined')

    conservante: Mapped[List[Conservantes]] = relationship('Conservantes', secondary=conservantes_picoles,
                                                           backref='conservantes', lazy='joined')

    aditivo_nutritivo: Mapped[List[AditivoNutritivo]] = relationship('AditivoNutritivo',
                                                                     secondary=aditivo_nutritivo_picole,
                                                                     backref='aditivos_nutritivos', lazy='joined')
