from sqlalchemy import Integer, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

import json
from typing import Iterable, List, Optional, Generator

from utils.model_base import Base

from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivoNutritivo
from models.ingredientes import Ingredientes
from models.sabores import Sabores
from models.tipo_picole import TiposPicole
from models.tipos_embalagem import TiposEmbalagem
from models.weak_tables import aditivo_nutritivo_picole, conservantes_picoles, ingredientes_picoles

from utils.helper import data_para_string


class Picoles(Base):

    __tablename__: str = "picoles"

    id: Mapped[int] = mapped_column("id", BigInteger, primary_key=True,
                                    autoincrement=True, nullable=False, unique=False)

    date_create: Mapped[datetime] = mapped_column("date_create", DateTime,
                                                  default=datetime.today, nullable=False)

    preco: Mapped[float] = mapped_column('preco', DECIMAL(8, 2), nullable=False)

    id_sabor: Mapped[int] = mapped_column("id_sabor", BigInteger,
                                          ForeignKey('sabores.id', name='fk_sabor_id', ondelete="CASCADE"),
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
                                                           backref='ingredientes', lazy='joined', cascade='delete')

    conservante: Mapped[Optional[List[Conservantes]]] = relationship('Conservantes', secondary=conservantes_picoles,
                                                                     backref='conservantes', lazy='joined', cascade='delete')

    aditivo_nutritivo: Mapped[Optional[List[AditivoNutritivo]]] = relationship('AditivoNutritivo',
                                                                               secondary=aditivo_nutritivo_picole,
                                                                               backref='aditivos_nutritivos', lazy='joined', cascade='delete')

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys() if not attr.startswith("_sa_instance_state")})}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()
