from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List

from utils.model_base import Base

# Weak Tables of `N=N` relations from `Picoles`


class AditivoNutritivoPicoles(Base):
    #  N=N of `aditivos_nutritivos with picoles`

    __tablename__: str = 'aditivo_nutritivo_picole'

    id_picole: Mapped[int] = mapped_column(BigInteger, ForeignKey('picoles.id'), nullable=False, primary_key=True)

    id_aditivo_nutritivo: Mapped[int] = mapped_column(BigInteger,
                                                      ForeignKey('aditivo_nutritivo.id'), nullable=False, primary_key=True)

    picole: Mapped["Picoles"] = relationship(back_populates='aditivo_nutritivo_association')

    aditivos_nutritivos: Mapped['AditivoNutritivo'] = relationship(back_populates='picole_association')


class IngredientesPicoles(Base):
    #  N=N of `ingredientes with picoles`

    __tablename__: str = 'ingredientes_picoles'

    id_picole: Mapped[int] = mapped_column(BigInteger, ForeignKey('picoles.id'), nullable=False, primary_key=True)

    id_ingredientes: Mapped[int] = mapped_column(BigInteger, ForeignKey('ingredientes.id'), nullable=False, primary_key=True)

    picole: Mapped['Picoles'] = relationship(back_populates='ingredientes_association')
    ingredientes: Mapped['Ingredientes'] = relationship(back_populates='picole_association')


class ConservantesPicoles(Base):
    #  N=N of `ingredientes with picoles`

    __tablename__: str = 'conservantes_picoles'

    id_picole: Mapped[int] = mapped_column(BigInteger, ForeignKey('picoles.id'), nullable=False, primary_key=True)

    id_conservantes: Mapped[int] = mapped_column(BigInteger, ForeignKey('conservantes.id'), nullable=False)

    picole: Mapped['Picoles'] = relationship(back_populates='conservantes_association')
    conservantes: Mapped['Conservantes'] = relationship(back_populates='picole_association')


class LotesNotasFiscais(Base):
    # N=N of `notas_fiscais with lotes`

    __tablename__: str = 'lotes_notas_fiscais'

    id_lote: Mapped[int] = mapped_column(BigInteger, ForeignKey('lotes.id'), primary_key=True)

    id_nota_fiscal: Mapped[int] = mapped_column(BigInteger, ForeignKey('notas_fiscais.id'), primary_key=True)

    lote: Mapped['Lotes'] = relationship(back_populates='nota_fiscal_association')
    nota_fiscal: Mapped['NotasFiscais'] = relationship(back_populates='lote_association')



