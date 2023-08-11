from typing import List

# Tables how objects
from models.sabores import Sabores
from models.aditivos_nutritivos import AditivoNutritivo
from models.revendedores import Revendedores
from models.picoles import Picoles

from utils.db_session import create_session
from utils.helper import data_para_string


def select_aditivo_nutritivo(id_table: int) -> None:
    with create_session() as db_handler, db_handler.begin():

        # Busca Simples, sem filtragem
        #datas_from: List[AditivoNutritivo] = db_handler.query(AditivoNutritivo)

        # Busca complexas, com filtros
        datas_from: List[AditivoNutritivo] = db_handler.query(AditivoNutritivo).filter(
            AditivoNutritivo.id == id_table).all()

        print("*** Datas From Table `Aditivo Nutritivo` ***")
        for line in datas_from:
            print(f"ID:\t{line.id}",
                  f"Data Create:\t{data_para_string(line.date_create)}",
                  f"Formula:\t{line.formula}",
                  f"Nome:\t{line.name}")


def select_sabores(id_table: int) -> None:
    with create_session() as db_handler, db_handler.begin():
        # Podemos também utilizar o comando `WHERE` já conhecido no sql em nossos objetos
        # Temos métodos que retornam valores caso a requisicão nao esteja em perssistência no db, segue abaixo os métodos
        # {'one()': `return uma raise 'Exception'`, 'one_or_none()': `return 'None' type or data request`, 'first()': `also return None`}
        datas_from: Sabores = db_handler.query(Sabores).where(Sabores.id == id_table).first()  # Return NoneType in Exception
        datas_from: Sabores = db_handler.query(Sabores).where(Sabores.id == id_table).one_or_none()  # Return NoneType in Exception
        datas_from: Sabores = db_handler.query(Sabores).where(Sabores.id == id_table).one()  # Return NoResultFound in Exception

        print("*** Datas from Table `Sabores` ***")
        print(f"ID:\t{datas_from.id}",
               f"Data Criacão:\t{data_para_string(datas_from.date_create)}",
               f"Sabor:\t{datas_from.sabor}")


def select_picole() -> None:
    with create_session() as db_handler, db_handler.begin():
        picoles: List[Picoles] = db_handler.query(Picoles).all()
        print('*** Datas from Table `Picoles` ***')

        for picole in picoles:

            print(f'(\n\n***\t--= Formnulário de Dados Picoles =--\t***\n\n)::\tID Picole: {picole.id}\n',
                  f'::\tData Criacao: {data_para_string(picole.date_create)}\n',
                  f'::\tValor: {picole.valor}\n\n',
                  f'::\tID Sabor: {picole.id_sabor}\n',
                  f'::\tSabor: {picole.sabor.sabor}\n\n',
                  f'::\tID Tipo Picole: {picole.id_tipos_picole}\n',
                  f"::\tTipo Picole: {picole.tipos_picole.name}\n\n",
                  f"::\tID Embalagem: {picole.id_tipo_embalagem}\n",
                  f"::\tEmbalagem: {picole.tipos_embalagem.name}\n\n",
                  f"::\tIngrediente: {picole.ingredientes}\n\n",
                  f"::\tConservantes: {picole.conservantes}\n\n",
                  f"::\tAditivo Nutritivo: {picole.aditivos_nutritivos}")


def select_order_by_sabores(id_table: int) -> None:
    # Organizando dados a partir de atributos

    with create_session() as db_handler, db_handler.begin():

        print("*** Datas from Table `Sabores` ***")

        # Utilizando range():
        for lines in range(1, id_table,  1):  # Para inverter `range(id_table, 1)
            print(lines)
            datas_from: List[Sabores] = db_handler.query(Sabores).where(Sabores.id == lines)
            for line in datas_from:
                print(f"ID:\t{line.id}",
                      f"Data Criacão:\t{data_para_string(line.date_create)}",
                      f"Sabor:\t{line.sabor}")


def select_group_by() -> None:

    #  Organizando por grupos, por pedrão toda consulta e organizada pelo `ID` da entidade
    # Podemos agrupar por um ou mais atributo
    with create_session() as db_handler, db_handler.begin():
        sabores: List[Sabores] = db_handler.query(Sabores).group_by(Sabores.id, Sabores.date_create)

        for sabor in sabores:
            ...


if __name__ == '__main__':
    # Tests selects:

    # -- `Aditivos Nutritivos`
    # Test Busca simples sem filtro >> OK
    #select_aditivo_nutritivo()

    # Tests Busca complexa, com filtros >>
    #select_aditivo_nutritivo(21)

    # -- `Sabores`
    # Tests Buscas complexas utilizando `WHERE` e métodos de filtragem  >> OK
    #select_sabores(21)
    # Tests ordenacão
    #select_order_by_sabores(30)

    # -- `Picoles`

    # Tests Consulta `Picole` >>
    select_picole()
