from sqlalchemy import ForeignKey, BigInteger, Column, Table


from utils.model_base import Base

# Weak Tables of `N=N` relations from `Picoles`


aditivo_nutritivo_picole = Table(
    'aditivo_nutritivo_picole',
    Base.metadata,
    Column('id_picole', BigInteger,
           ForeignKey('picoles.id',
                      name='fk_picole_id',
                      ondelete="CASCADE"), primary_key=True, nullable=False, index=True),
    Column('id_aditivo_nutritivo', BigInteger,
           ForeignKey('aditivos_nutritivos.id',
                      name='fk_aditivo_nutritivo_id',
                      ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)

conservantes_picoles = Table(
    'conservantes_picoles',
    Base.metadata,
    Column('id_picole', BigInteger,
           ForeignKey('picoles.id',
                      name='fk_picole_id',
                      ondelete="CASCADE"), primary_key=True, index=True, nullable=False),
    Column('id_conservante', BigInteger,
           ForeignKey('conservantes.id',
                      name='fk_conservante_id',
                      ondelete="CASCADE"), primary_key=True, index=True, nullable=False)
)

ingredientes_picoles = Table(
    'ingredientes_picole',
    Base.metadata,
    Column('id_picole', BigInteger,
           ForeignKey('picoles.id',
                      name='fk_picole_id',
                      ondelete="CASCADE"), primary_key=True, nullable=False, index=True),
    Column('id_ingrediente', BigInteger,
           ForeignKey('ingredientes.id',
                      name='fk_ingrediente_id',
                      ondelete="CASCADE"), primary_key=True, nullable=False, index=True)
)


lotes_notas_fiscais = Table(
    'lotes_notas_fiscais',
    Base.metadata,
    Column('id_lote', BigInteger,
           ForeignKey('lotes.id',
                      ondelete='CASCADE',
                      name='fk_lote_id'),
           primary_key=True, nullable=False),

    Column('id_notas_fiscais', BigInteger,
           ForeignKey('notas_fiscais.id',
                      ondelete='CASCADE',
                      name='fk_notas_fiscais_id'),
           primary_key=True, nullable=False)
)
