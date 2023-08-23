from sqlalchemy import select

import asyncio
from typing import Dict

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

from utils.db_session import create_session
from utils.helper import data_para_string


async def select_aditivo_nutritivo() -> None:
    async with create_session() as handler:
        print("***\tInformacoes Tabela Aditivos Nutritivos\t***")
        #  Buscando
        aditivo_nutritivo: AditivoNutritivo = await handler.scalar(select(AditivoNutritivo).where(AditivoNutritivo.id == int(input("::\tBuscar por ID: "))))
        print(f"::\tID:\t{aditivo_nutritivo.id}\n::\tDATA CRIACAO:{data_para_string(aditivo_nutritivo.date_create)}\n::\tNOME:\t{aditivo_nutritivo.nome}\n::\tFORMULA QUIMICA:\t{aditivo_nutritivo.formula_quimica}")


async def select_sabores() -> None:
    print("\n\n***\tInformacões Tabela Sabores\t***")
    async with create_session() as handler:
        sabor: Sabores = await handler.scalar(select(Sabores).where(Sabores.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{sabor.id}\n::\tDATA CRIACÃO:\t{sabor.date_create}\n::\tNOME:\t{sabor.nome}")


async def select_tipos_embalagem() -> None:
    print("\n\n***Informacões da Tabela Tipos Embalagem\t***")
    async with create_session() as handler:
        tipos_embalagem: TiposEmbalagem = await handler.scalar(select(TiposEmbalagem).where(TiposEmbalagem.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{tipos_embalagem.id}\n::\tDATA CRIACÃO:\t{tipos_embalagem.data_create}\n::\tNOME:\t{tipos_embalagem.nome}")


async def select_tipos_picole() -> None:
    print("\n\n***\tInformacões Tabela Tipos Picole\t***")
    async with create_session() as handler:
        tipos_picole: TiposPicole = await handler.scalar(select(TiposPicole).where(TiposPicole.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{tipos_picole.id}\n::\tDATA CRIACÃO:\t{tipos_picole.date_create}\n::\tNOME:\t{tipos_picole.nome}")

async def select_ingredientes() -> None:
    print("\n\n***\tinformacoes Tabela Ingredientes\t***")
    async with create_session() as handler:
        ingredientes: Ingredientes = await handler.scalar(select(Ingredientes).where(Ingredientes.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{ingredientes.id}\n::\tDATA CRIACÃO:\t{ingredientes.date_create}\n::\tNOME:\t{ingredientes.nome}")


async def select_conservantes() -> None:
    print("\n\n***\tinformacoes Tabela Conservantes\t***")
    async with create_session() as handler:
        conservantes: Conservantes = await handler.scalar(select(Conservantes).where(Conservantes.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{conservantes.id}\n::\tDATA CRIACÃO:\t{conservantes.date_create}\n::\tNOME:\t{conservantes.nome}\n::\tDESCRICÃO:\t{conservantes.descricao}")


async def select_revendedores() -> None:
    print("\n\n***\tinformacoes Tabela Revendedores\t***")
    async with create_session() as handler:
        revendedor: Revendedores = await handler.scalar(select(Revendedores).where(Revendedores.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{revendedor.id}\n::\tDATA CRIACÃO:\t{revendedor.date_create}\n::\tCNPJ:\t{revendedor.cnpj}\n::\tRAZÃO SOCIAL:\t{revendedor.razao_social}\n::\tCONTATO:\t{revendedor.contato}")


async def select_lotes() -> None:
    print("\n\n***\tinformacoes Tabela Lotes\t***")
    async with create_session() as handler:
        lote: Lotes = await handler.scalar(select(Lotes).where(Lotes.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{lote.id}\n::\tDATA CRIACÃO:\t{lote.date_create}\n::\tQUANTIDADE:\t{lote.quantidade}\n::\tTIPO PICOLE:\t{lote.tipos_picole.nome}\n::\tID TIPO PICOLE:\t{lote.id_tipos_picole}")


async def select_notas_fiscais() -> None:
    print("\n\n***\tinformacoes Tabela Notas Fiscais\t***")
    async with create_session() as handler:
        nota_fiscal: NotasFiscais = await handler.scalar(select(NotasFiscais).where(NotasFiscais.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{nota_fiscal.id}\n::\tDATA CRIACÃO:\t{nota_fiscal.date_create}\n::\tVALOR:\t{nota_fiscal.valor}\n::\tNÚMERO DE SÉRIE:\t{nota_fiscal.numero_serie}\n::\tDESCRICAO:\t{nota_fiscal.descricao}\n::\tREVENDEDOR:\t{nota_fiscal.revendedor.contato}\n")
        for line in nota_fiscal.lotes:
            print(f"::\tID LOTE:\t{line.id}\n::\tQUANTIDADE LOTE:\t{line.quantidade}")


async def select_picoles() -> None:
    print("\n\n***\tinformacoes Tabela Picoles\t***")
    async with create_session() as handler:
        picole: Picoles = await handler.scalar(select(Picoles).where(Picoles.id == int(input("::\tBuscar Por ID: "))))
        print(f"::\tID:\t{picole.id}\n::\tDATA CRIACÃO:\t{picole.date_create}\n::\tPRECO:\t{picole.preco}\n::\tID SABOR:\t{picole.id_sabor}\n::\tID TIPO EMBALAGEM:\t{picole.id_tipos_embalagem}\n::\tID TIPO PICOLE:\t{picole.id_tipos_picole}")

        for ingrediente in picole.ingrediente:
            print(f"\n::\tINGREDIENTE:\t{ingrediente.nome}")

        for conservante in picole.conservante:
            print(f"\n::\tCONSERVANTE:\t{conservante.nome}\n::\tCONSERVANTE DESCRICAO:\t{conservante.descricao}")

        for aditivo_nutritivo in picole.aditivo_nutritivo:
            print(f"\n::\tADITIVO NUTRITIVO:\t{aditivo_nutritivo.nome}\n::\tFORMULA QUIMICA ADITIVO:\t{aditivo_nutritivo.formula_quimica}")


def select_main() -> None:
    maker = asyncio.get_event_loop()  # Start handler

    #maker.run_until_complete(select_aditivo_nutritivo())
    #maker.run_until_complete(select_sabores())
    #maker.run_until_complete(select_tipos_embalagem())
    #maker.run_until_complete(select_tipos_picole())
    #maker.run_until_complete(select_ingredientes())
    #maker.run_until_complete(select_conservantes())
    #maker.run_until_complete(select_revendedores())
    #maker.run_until_complete(select_lotes())
    #maker.run_until_complete(select_notas_fiscais())
    #maker.run_until_complete(select_picoles())


if __name__ == '__main__':
    # Tests selects:
    select_main()
