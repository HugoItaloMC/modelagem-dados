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
    nome: str = input("::\tNome :")
    formula_quimica: str = input("::\tformula Quimica: ")

    aditivos_nutritivos: AditivoNutritivo = AditivoNutritivo(name=nome,
                                                             formula=formula_quimica)
    with create_session() as db_handler, db_handler.begin():
        db_handler.add(aditivos_nutritivos)

    return aditivos_nutritivos

def insert_sabores() -> Sabores:
    #  Insert data in `Sabores`

    print("** Insert data in table `Sabores` **")
    sabor: str = input("::\tNome: ")
    sabores: Sabores = Sabores(sabor=sabor)

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(sabores)
    return sabores


def insert_tipos_embalagems() -> TiposEmbalagem:
    # Insert data in `TiposEmbalagems`

    print("** Insert data in table `Tipos Embalagems` **")
    nome: str = input("::\tName:  ")
    tipos_embalagem: TiposEmbalagem = TiposEmbalagem(name=nome)

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(tipos_embalagem)

    return tipos_embalagem


def insert_tipos_picole() -> TiposPicole:
    # Insert data in `Tipos Picole`

    print('** Insert Data in Table `Tipos Picole` **')
    nome: str = input("::\tNome:  ")
    tipos_picole: TiposPicole = TiposPicole(name=nome)
    with create_session() as db_handler, db_handler.begin():
        db_handler.add(tipos_picole)

    return tipos_picole


def insert_ingredientes() -> Ingredientes:
    # Insert data in Table `Ingredientes`

    print("** Cadastrando Ingrediente **")
    nome : str = input("::\tNome:  ")
    ingrediente: Ingredientes = Ingredientes(name=nome)

    with create_session() as db_hander, db_hander.begin():
        db_hander.add(ingrediente)
    return ingrediente


def insert_conservantes() -> None:
    # insert data in Table `Conservantes`
    print("Insert data in Table `Conservantes` **")
    nome: str = input("::\tNome:  ")
    descricao: str = input("::\tDescricao:  ")

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(Conservantes(name=nome, descricao=descricao))


def insert_revendedores() -> Revendedores:
    # Insert data in `Revendedores`

    print("Insert data in Table `Revendedores` **")

    cnpj: int = input('::\tCNPJ:  ')
    razao_social: str = input("::\tRazao Social:  ")
    contato: str = input("::\tContato:  ")
    revendedor: Revendedores = Revendedores(cnpj=cnpj,
                                            razao_social=razao_social, contato=contato)

    with create_session() as db_handler, db_handler.begin():
        db_handler.add(revendedor)

    return revendedor


def insert_lotes() -> None:
    # Insert data in Table `Lotes`
    print("Insert Data in Tables `Lotes` **")
    id_tipo_picole: int = input("::\tInforme ID do tipo de picole do Lote:  ")
    quantidade: int = input("\n::\tQuantidade:  ")

    with create_session() as db_hander, db_hander.begin():
        db_hander.add(Lotes(id_tipos_picole=id_tipo_picole, quantidade=quantidade))


def insert_notas_fiscais() -> None:
    # Insert data in table `Notas Fiscais`
    print("** Insert data in Table `Notas Fiscais` **")
    valor: float = input("::\tValor :")
    numero_serie: str = input("::\tNumero de Serie:  ")
    descricao: str = input("::\tDescricao:  ")

    # Para teste vamos cadastrar um novo revendedor dentro deste método
    revendedor: Revendedores = insert_revendedores()

    with create_session() as db_handler, db_handler.begin():
       db_handler.add(NotasFiscais(id_revendedor=revendedor.id, valor=valor,
                                   numero_serie=numero_serie, descricao=descricao))


def insert_picoles() -> None:
    # Insert data in `Picole`

    print("** Cadastrando Picoles **")

    valor: float = input("::\tValor:  ")
    ingrediente: Ingredientes = insert_ingredientes()

    id_sabor: int = input("::\tID Sabor:  ")
    id_tipo_embalagem: int = input("::\tID Tipos Embalagems:  ")
    id_tipo_picoles: int = input("::\tID Tipos Picoles:  ")

    try:
        with create_session() as db_handler, db_handler.begin():
            picole: Picoles = Picoles(valor=valor,
                                     id_sabor=db_handler.execute(select(Sabores).where(Sabores.id == id_sabor)),

                                     id_tipo_embalagem=db_handler.execute(select(TiposEmbalagem)
                                                                         .where(TiposEmbalagem.id == id_tipo_embalagem
                                                                                 )),
                                     id_tipos_picole=db_handler.execute(select(TiposPicole)
                                                                         .where(TiposPicole.id == id_tipo_picoles)
                                                                         ))
            db_handler.add(picole)

    except Exception as err:

        while op := input("**\tATIVOS INEXISTENTES\t**\ngostaria de cadastrar novos ativos?\n[Y/N]\n::\t"
                                .lower()) != 'n':
            if op == 'Y' and err:
                sabor: Sabores = insert_sabores()
                tipo_embalagem: TiposEmbalagem = insert_tipos_embalagems()
                tipos_picoles: TiposPicole = insert_tipos_picole()
                with create_session() as db_handler, db_handler.begin():
                    picole: Picoles = Picoles(valor=valor, id_sabor=sabor.id,
                                          id_tipo_embalagem=tipos_picoles.id, id_tipos_picole=tipos_picoles.id)
                    return db_handler.add(picole)

    else:
        picole.ingredientes.append(ingrediente)


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
    #insert_picoles()
    ...
