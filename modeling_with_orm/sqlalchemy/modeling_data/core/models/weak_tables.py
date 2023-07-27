from sqlalchemy import Column, Table, Integer, ForeignKey

from utils.model_base import Base

# Weak Tables of `N=N` relations

#  N=N of `aditivos_nutritivos with picoles`
aditivos_nutritivos_picole = Table(
    'aditivos_nutritivos_picole',  # Name Table
    Base.metadata,  # Built'in Setting on SQLAlchemy to create weak tables
    # Attrs from tables with datas
    Column('id_picole', Integer, ForeignKey('picoles.id', name='fk_picole')),
    Column('id_aditivo_nutritivo', Integer, ForeignKey('aditivo_nutritivo.id', name='fk_aditivo_nutritivo'))
)

#  N=N of `ingredientes with picoles`
ingredientes_picoles = Table(
    'ingredientes_picole',
    Base.metadata,
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_ingredientes', Integer, ForeignKey('ingredientes.id'))
)

#  N=N of `conservantes with picoles`
conservantes_picoles = Table(
    'conservantes_picoles',
    Base.metadata,
    Column('id_picoles', Integer, ForeignKey('picoles.id')),
    Column('id_conservantes', Integer, ForeignKey('conservantes.id'))
)

lotes_notas_fiscais = Table(
    'lotes_notas_fiscais',
    Base.metadata,
    Column('id_lote', Integer, ForeignKey('lotes.id')),
    Column('id_notas_fiscais', Integer, ForeignKey('notas_fiscais.id'))
)
