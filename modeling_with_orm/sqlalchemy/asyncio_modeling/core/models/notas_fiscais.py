from sqlalchemy import String, BigInteger, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
import json
from typing import Iterable, List, Generator

from utils.model_base import Base
from utils.helper import data_para_string
from models.revendedores import Revendedores
from models.lotes import Lotes
from models.weak_tables import lotes_notas_fiscais


class NotasFiscais(Base):

    __tablename__: str = "notas_fiscais"

    id: Mapped[int] = mapped_column("id", BigInteger, primary_key=True, autoincrement=True, unique=True)

    date_criate: Mapped[datetime] = mapped_column("date_create", DateTime, default=datetime.today)

    valor: Mapped[float] = mapped_column("valor", DECIMAL(8, 2), nullable=False)

    numero_serie: Mapped[str] = mapped_column("numero_serie", String(45), nullable=False, index=True)

    descricao: Mapped[str] = mapped_column("descricao", String(70), nullable=False)

    id_revendedor: Mapped[Revendedores] = mapped_column('id_revendedor', BigInteger,
                                                        ForeignKey('revendedores.id',
                                                                   name='fk_revendedor_id',
                                                                   ondelete='CASCADE'),
                                                        primary_key=True, nullable=False, index=True)

    revendedor: Mapped[List[Revendedores]] = relationship('Revendedores', lazy='joined', cascade='delete')

    lotes: Mapped[List[Lotes]] = relationship('Lotes', secondary=lotes_notas_fiscais, backref='lotes', lazy='dynamic')
