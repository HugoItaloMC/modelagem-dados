# Módulo auxiliar para povoar o banco de dados `fabrica de picoles`

from tqdm import tqdm
from sqlmodel import select

from time import sleep
from typing import List

from utils.db_session import create_session
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

from utils.helper import gerar_float, gerar_string, gerar_inteiros, data_para_string, string_hexadecimal


# Functions to Populate Tables >>
def populate_aditivos_nutritivos() -> None:
    # 1 -- Aditivos Nutritivos`
        print("***\tPopulano Tabela Aditivos Nutritivos\t***")
        with create_session() as handler, handler.begin():
            for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
                handler.add(AditivoNutritivo(nome=gerar_string(), formula_quimica=gerar_string(frase=True)))
            sleep(0.3)


def populate_sabores() -> None:
    # 2 -- `Sabores`
        print("***\tPopulano Tabela Sabores\t***")
        with create_session() as handler, handler.begin():
            for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
                handler.add(Sabores(nome=gerar_string()))
            sleep(0.3)


def populate_tipos_embalagem() -> None:
    # 3 -- `Tipos Embalagem`
    print("***\tPopulano Tabela Tipos Embalagem\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            handler.add(TiposEmbalagem(nome=gerar_string()))
        sleep(0.3)


def populate_tipos_picole() -> None:
    # 4 -- `Tipos Picole`
    print("***\tPopulano Tabela Tipos Picole\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            handler.add(TiposPicole(nome=gerar_string()))
        sleep(0.3)


def populate_ingredientes() -> None:
    # 5 --  `Ingredientes`
    print("***\tPopulano Tabela Ingredientes\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            handler.add(Ingredientes(nome=gerar_string()))
        sleep(0.3)


def populate_conservantes() -> None:
    # 6 -- `Conservantes`
    print("***\tPopulano Tabela Conservantes\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            handler.add(Conservantes(nome=gerar_string(), descricao=gerar_string(frase=True)))
        sleep(0.3)


def populate_revendedores() -> None:
    # 7 -- `Revendedores`
    print("***\tPopulano Tabela Revendedores\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            handler.add(Revendedores(cnpj=str(gerar_float(digitios=4)),
                                     razao_social=gerar_string(frase=True),
                                     contato=gerar_string()))
        sleep(0.3)


def populate_lotes() -> None:
    # 8 -- `Lotes`
    print("***\tPopulano Tabela Lotes\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            handler.add(Lotes(quantidade=gerar_inteiros(), id_tipos_picole=gerar_inteiros()))
        sleep(0.3)


def populate_notas_fiscais() -> None:
    # 9 -- `Notas Fiscais`
    print("***\tPopulano Tabela Notas Fiscais\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc="Carregando...", colour=string_hexadecimal()):
            nota_fiscal: NotasFiscais = NotasFiscais(valor=gerar_float(digitios=3),
                                                     numero_serie=string_hexadecimal(),
                                                     descricao=gerar_string(frase=True),
                                                     id_revendedor=gerar_inteiros())
            lote: Lotes = handler.execute(select(Lotes).where(Lotes.id == gerar_inteiros()))
            nota_fiscal.lote.append(lote)
            handler.add(nota_fiscal)
        sleep(0.3)


def populate_picoles() -> None:
    # 10 -- `Picoles`
    print("***\tPopulando Tabela Picoles\t***")
    with create_session() as handler, handler.begin():
        for _ in tqdm(range(1, 101), desc='Carregando...'):
            picole: Picoles = Picoles(preco=gerar_float(digitios=1),
                                      id_sabor=gerar_inteiros(),
                                      id_tipo_embalagem=gerar_inteiros(),
                                      id_tipos_picole=gerar_inteiros())

            ingrediente: List[Ingredientes] = handler.execute(select(Ingredientes).where(Ingredientes.id == gerar_inteiros()))
            picole.ingrediente.append(ingrediente)

            conservante: List[Conservantes] = handler.execute(select(Conservantes).where(Conservantes.id == gerar_inteiros()))
            picole.conservantes.append(conservante)

            aditivo_nutritivo: List[AditivoNutritivo] = handler.execute(select(AditivoNutritivo).where(AditivoNutritivo.id == gerar_inteiros()))
            picole.aditivo_nutritivo.append(aditivo_nutritivo)
            handler.add(picole)



if __name__ == '__main__':
    # Run Populate
    # Tests Populates Tables >>

    populate_aditivos_nutritivos()  # `AditivosNutritivos` >> OK
    populate_sabores()  # `Sabores` >> OK
    populate_tipos_embalagem()  # `Tipos Embalagem` >> OK
    populate_tipos_picole()  # `Tipos Picole` >> OK
    populate_ingredientes()  # `Ingredientes` >> OK
    populate_conservantes()  # `Conservantes` >> OK
    populate_revendedores()  # `Revendedores` >> (ERRO AO UTILIZAR `gerar_inteiros()` ao attr `cnpj`)
    populate_lotes()  # `Lotes` >> OK
    populate_notas_fiscais()  # `Notas Fiscais` >> OK
    populate_picoles()  # `Picoles` >> OK
