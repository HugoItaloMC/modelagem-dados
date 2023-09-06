from sqlmodel import select, join

import json
from typing import Iterable, List

# Tables how objects
from models.aditivos_nutritivos import AditivoNutritivo
from models.sabores import Sabores
from models.tipos_embalagem import TiposEmbalagem
from models.tipo_picole import TiposPicole
from models.ingredientes import Ingredientes
from models.conservantes import Conservantes
from models.revendedores import Revendedores
from models.lotes import Lotes
from models.notas_fiscais import NotasFiscais
from models.picoles import Picoles

from models.weak_tables import LotesNotasFiscais

from utils.db_session import create_session
from utils.helper import data_para_string

#    Para consultas utilizando SQL-Model, podemos utilizar o próprio handler `create_session` que é um objeto do tipo
#  `sqlmodel.Session` e também `sqlmodel.select` ou os objetos `sqlalchemy.future.select` e `sqlalchemy.select`
#  para realizar consultas ao DB.


def select_aditivo_nutritivo() -> None:
    # Utilizando o handler desenvolvido no projeto
    with create_session() as handler, handler.begin():
        print("***\tSelecionando Itens Tabela Aditivos Nutritivos\t***")
        # aditivos_nutritivos: AditivoNutritivo = handler.query(AditivoNutritivo).first()
        # print(aditivos_nutritivos)

         # Utilizando `sqlmodel.select`
        print("\n".join(map(str, handler.scalars(select(AditivoNutritivo)))))


def select_sabores() -> None:
    with create_session() as db_handler, db_handler.begin():
        # Filtrando por ID
        sabor: Iterable[Sabores] = db_handler.scalars(select(Sabores).where(Sabores.id == int(input("::\tBuscar Por ID: "))))
        print("\n".join(map(str, sabor)))


def tipos_embalagem_join_tipos_picole() -> None:
    with (create_session() as handler, handler.begin()):
        # Um exemplo trivial de join utilizando sql-model
        print("\n".join(map(str, handler.scalars(select(TiposEmbalagem, TiposPicole).select_from(join(TiposEmbalagem, TiposPicole, TiposEmbalagem.id == TiposPicole.id)).limit(25)))),
              "\n".join(map(str, handler.scalars(select(TiposPicole, TiposEmbalagem).select_from(join(TiposPicole, TiposEmbalagem, TiposPicole.id == TiposEmbalagem.id)).limit(25)))))


def select_group_conservantes_ingredientes() -> None:
    # Um exemplo trivial de `group`
    with create_session() as handler, handler.begin():
        print("\n".join(map(str, handler.scalars(select(Conservantes).group_by(Conservantes.date_create, Conservantes.id)))))


def select_revendedor() -> None:
    with create_session() as handler:
        print("\n".join(map(str, handler.scalars(select(Revendedores).order_by(Revendedores.cnpj)))))


def lote_join_tipos_picole() -> None:
    with create_session() as handler:
        lotes = handler.exec(select(Lotes))
        for lines in lotes:
            for line in lines.tipo_picole:
                print(lines) if line.id == int(input("::\tBuscar Lote por ID Tipos Picole\nID:\t")) else ...


def nota_fisical_join_lote() -> None:
    with create_session() as handler:
        nota_fiscal: NotasFiscais = handler.scalars(select(NotasFiscais))
        id_lote: int = int(input("::\tBuscar Nota Fiscal por ID Lote\nID:\t"))
        print(" ".join(map(str, [line for line in nota_fiscal.unique().all() if any(lote.id == id_lote for lote in line.lote)])))


def nota_fiscal_join_revendedor() -> None:
    with create_session() as handler:
        print("\n".join(map(str, handler.scalars(select(NotasFiscais).select_from(join(NotasFiscais, Revendedores, Revendedores.id == int(input("::\tBuscar Nota Fiscal por ID Revendedor\nID: "))))))))


def picole_join_all() -> None:
    # Buscas em relacionamentos  1=n
    with create_session() as handler:
        # Select Picole Join Sabores
        print("\n\n".join(map(str, handler.exec(select(Picoles).select_from(join(Picoles, Sabores)).where(Sabores.id == int(input("::\tBuscar Picole por ID Sabor\nID: ")))).unique().all())))

        # Select Picole Join Tipos Embalagem
        print("\n\n".join(map(str, handler.exec(select(Picoles).select_from(join(Picoles, TiposEmbalagem)).where(TiposEmbalagem.id == int(input("::\tBuscar Picole por ID Tipos Embalagem\nID: ")))).unique().all())))

        picoles: Picoles = handler.exec(select(Picoles).where(Picoles.id == int(input("\n::\tBuscar Picole por ID\nID: ")))).unique().all()
        for picole in picoles:
            print(f"::\tID:\t{picole.id}\n::\tDATA CRIACÃO:\t{picole.date_create}\n::\tINGREDIENTE:\t{picole.ingrediente}\n::\tCONSERVANTE:\t{picole.conservantes}\n::\tADITIVO-NUTRITIVO:\t{picole.aditivo_nutritivo}")


if __name__ == '__main__':
    #  Tests QUERYS >>
    #select_aditivo_nutritivo()
    #select_sabores()
    #tipos_embalagem_join_tipos_picole()
    #select_group_conservantes_ingredientes()
    #select_revendedor()
    #lote_join_tipos_picole()
    #nota_fisical_join_lote()
    #nota_fiscal_join_revendedor()
    picole_join_all()

