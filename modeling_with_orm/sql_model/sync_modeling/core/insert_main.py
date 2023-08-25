"""
Learning how to insert data into objects with SQLAlchemy `orm` Python,
In this module, data will be entered individually and manually
"""

from sqlalchemy import select

import asyncio

# Import Handler how `sessionmaker and Session` of SQLAlchemy
from utils.db_session import create_session

# Import Models in modules `py` how objects
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

#  Insert data to entity how object


def insert_aditivos_nutritivos() -> None:
    # Insert data  `aditivos_nutritivos` >>
    print("** Insert Data in table `Aditivos Nutritivos` **")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(AditivoNutritivo(nome=input("::\tNome :"), formula_quimica=input("::\tformula Quimica: ")))


def insert_sabores() -> None:
    #  Insert data in `Sabores`

    print("** Insert data in table `Sabores` **")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(Sabores(nome=input("::\tNome: ")))


def insert_tipos_embalagems() -> None:
    # Insert data in `TiposEmbalagems`

    print("** Insert data in table `Tipos Embalagems` **")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(TiposEmbalagem(nome=input("::\tNome: ")))


def insert_tipos_picole() -> None:
    # Insert data in `Tipos Picole`

    print('** Insert Data in Table `Tipos Picole` **')

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(TiposPicole(nome=input("::\tNome: ")))


def insert_ingredientes() -> Ingredientes:
    # Insert data in Table `Ingredientes`

    print("** Cadastrando Ingrediente **")

    with create_session() as db_hander, db_hander.begin():
        db_hander.add(Ingredientes(nome=input("::\tNome: ")))


def insert_conservantes() -> None:
    # insert data in Table `Conservantes`
    print("Insert data in Table `Conservantes` **")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(Conservantes(nome=input("::\tNome "), descricao=input("::\tDescricão: ")))


def insert_revendedores() -> None:
    # Insert data in `Revendedores`

    print("Insert data in Table `Revendedores` **")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(Revendedores(cnpj=input("::\tCNPJ: "),
                                    razao_social=input("::\tRAZÃO SOCIAL: "),
                                    contato=input("::\tCONTATO: ")))


def insert_lotes() -> None:
    # Insert data in Table `Lotes`
    print("Insert Data in Tables `Lotes` **")

    with create_session() as db_hander, db_hander.begin():
        db_hander.add(Lotes(id_tipos_picole=int(input("::\tID TIPO PICOLE: ")), quantidade=int(input("QUANTIDADE: "))))


def insert_notas_fiscais() -> None:
    # Insert data in table `Notas Fiscais`
    print("** Insert data in Table `Notas Fiscais` **")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(NotasFiscais(id_revendedor=int(input("::\tID REVENDEDOR: ")), valor=float(input("::\tVALOR: ")),
                                    numero_serie=input("::\tNUMERO DE SÉRIE:"), descricao=input("DESCRICÃO: ")))
()

def insert_picoles() -> None:
    # Insert data in `Picole`

    print("** Cadastrando Picoles **")

    with create_session() as handler, handler.begin():
        picole: Picoles = Picoles(preco=float(input("::\tPRECO: ")),
                                 id_sabor=int(input("::\tID SABOR: ")),
                                 id_tipo_embalagem=int(input("::\tID TIPO EMBALAGEM")),
                                 id_tipo_picole=int(input("::\tID TIPO PICOLE: ")))
        ingrediente: Ingredientes = handler.execute(select(Ingredientes).where(Ingredientes.id == int(input("::\tID INGREDIENTE"))))
        picole.ingrediente.append(ingrediente)

        conservante: Conservantes = handler.execute(select(Conservantes).where(Conservantes.id == int(input("::\tID CONSERVANTE: "))))
        picole.conservantes.append(conservante)

        aditivo_nutritivo: AditivoNutritivo = handler.execute(select(AditivoNutritivo).where(AditivoNutritivo.id == int(input("::\tID ADITIVO NUTRITIVO: "))))
        picole.aditivo_nutritivo.append(aditivo_nutritivo)

        handler.add(picole)

if __name__ == '__main__':

    # 1 -- Tests Insert data `Aditivos Nutritivos` >> OK
    #insert_aditivos_nutritivos()

    # 2 -- Tests insertt Data `Sabores` >> OK
    #insert_sabores()

   # 3 -- Tests insert data `Tipos Embalagems` >> OK
    #insert_tipos_embalagems()

    # 4 -- Tests insert data `Tipos Picoles` >> OK
    #insert_tipos_picole()

    # 5 -- Tests insert data `Ingredientes` >> OK
    #insert_ingredientes()

    # 6 -- Tests insert data `Conservantes` >> OK
    #insert_conservantes()

    # 7 -- Tests insert data `Revendedores` >> OK
    #insert_revendedores()

    # 8 -- Tests insert data `Lotes` >> ...
    #insert_lotes()

    # 9 -- Insert data `Notas Fiscais`
    #insert_notas_fiscais()

    # 10 -- Insert data `Picoles`
    insert_picoles()

