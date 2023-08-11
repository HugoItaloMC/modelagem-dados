# Módulo auxiliar para povoar o banco de dados `fabrica de picoles`

from tqdm import tqdm
from sqlalchemy import select
from sqlalchemy.orm import Session

from time import sleep

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
from models.weak_tables import AditivoNutritivoPicoles, ConservantesPicoles, IngredientesPicoles

# Functions to Populate Tables >>

# 1 -- Aditivos Nutritivos`


def populate_aditivos_nutritivos() -> None:
        db_handler: Session = create_session()
        gerar_cor: str = string_hexadecimal()
        # The package `tqdm` create custom loading bar
        for n in tqdm(range(1, 101),  # Sized Loop
                      desc="Cadastrando",  # Bar description
                      colour=gerar_cor):  # Loading Bar Color
            nome: str = gerar_string(frase=True)
            formula: str = gerar_string()
            db_handler.add(AditivoNutritivo(name=nome, formula=formula))
            sleep(0.5)
        db_handler.commit()
        db_handler.close()
        sleep(0.5)


# 2 -- `Sabores`


def populate_sabores() -> None:

    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        sabor: str = gerar_string()
        db_handler.add(Sabores(sabor=sabor))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)


# 3 -- `Tipos Embalagem`


def populate_tipos_embalagem() -> None:
    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        nome: str = gerar_string()
        db_handler.add(TiposEmbalagem(name=nome))
    db_handler.commit()
    db_handler.close()


# 4 -- `Tipos Picole`

def populate_tipos_picole() -> None:

    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        nome: str = gerar_string()
        db_handler.add(TiposPicole(name=nome))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)


# 5 --  `Ingredientes`


def populate_ingredientes() -> None:

    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        nome: str = gerar_string()
        db_handler.add(Ingredientes(name=nome))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)


# 6 -- `Conservantes`


def populate_conservantes() -> None:
    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        nome: str = gerar_string()
        descricao: str = gerar_string(frase=True)
        db_handler.add(Conservantes(name=nome, descricao=descricao))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)


# 7 -- `Revendedores`


def populate_revendedores() -> None:
    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):

        cnpj: str = gerar_string()
        razao_social: str = gerar_string(frase=True)
        contato: str = gerar_string()
        db_handler.add(Revendedores(cnpj=cnpj, razao_social=razao_social, contato=contato))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)

# 8 -- `Lotes`


def populate_lotes() -> None:
    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        id_tipo_picole: int = gerar_inteiros()
        quantidade: int = gerar_inteiros()
        db_handler.add(Lotes(id_tipos_picole=id_tipo_picole, quantidade=quantidade))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)


# 9 -- `Notas Fiscais`


def populate_notas_fiscais() -> None:

    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):
        valor: float = gerar_float(digitios=3)
        numero_serie: str = string_hexadecimal()
        descricao: str = gerar_string(frase=True)
        id_revendedor: int = gerar_inteiros()

        db_handler.add(NotasFiscais(valor=valor, numero_serie=numero_serie,
                                    descricao=descricao, id_revendedor=id_revendedor))

    db_handler.commit()
    db_handler.close()
    sleep(0.5)


# 10 -- `Picoles`


def populate_picoles() -> None:

    db_handler: Session = create_session()
    gerar_cor: str = string_hexadecimal()

    for _ in tqdm(range(1, 101), desc="Carregando...", colour=gerar_cor):

        picoles: Picoles = Picoles(valor=gerar_float(), id_sabor=gerar_inteiros(), id_tipo_embalagem=gerar_inteiros(),
                                   id_tipos_picole=gerar_inteiros())

        picoles.ingredientes_association.append(IngredientesPicoles(ingredientes=Ingredientes(name=gerar_string())))

        random_: float = gerar_float()
        if random_ > 4:
            for _ in range(4):
                picoles.aditivo_nutritivo_association.append(AditivoNutritivoPicoles(
                    aditivos_nutritivos=AditivoNutritivo(name=gerar_string(), formula=gerar_string(frase=True))))

        else:
            for _ in range(4):
                picoles.conservantes_association.append(ConservantesPicoles(conservantes=Conservantes(
                    name=gerar_string(), descricao=gerar_string(frase=True))))

        db_handler.add(picoles)

    db_handler.commit()
    sleep(0.5)


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