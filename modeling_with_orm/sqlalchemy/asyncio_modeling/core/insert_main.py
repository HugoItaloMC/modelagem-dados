"""
Learning to insert data into objects with SQLAlchemy `orm` Python,
In this module, data will be entered individually and manually
"""

from sqlalchemy import select

import asyncio
from typing import Coroutine, List

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

# Weak Tables
from models.weak_tables import (IngredientesPicoles,
                                ConservantesPicoles,
                                AditivoNutritivoPicoles,
                                LotesNotasFiscais)

#  Insert data to entity how object


async def insert_aditivos_nutritivos() -> AditivoNutritivo:
    # Insert data  `aditivos_nutritivos` >>
    print("** Insert Data in table `Aditivos Nutritivos` **")
    aditivos_nutritivos: AditivoNutritivo = AditivoNutritivo(name=input("::\tNome :"),
                                                             formula=input("::\tformula Quimica: "))
    async with create_session() as db_handler:
        db_handler.add(aditivos_nutritivos)
        await db_handler.commit()

        return aditivos_nutritivos


async def insert_sabores() -> Sabores:
    #  Insert data in `Sabores`

    print("** Insert data in table `Sabores` **")
    sabores: Sabores = Sabores(sabor=input("::\tNome: "))

    async with create_session() as db_handler:
        db_handler.add(sabores)
        await db_handler.commit()

        return sabores


async def insert_tipos_embalagems() -> TiposEmbalagem:
    # Insert data in `TiposEmbalagems`

    print("***\tInsert data in table `Tipos Embalagems`\t***")

    tipos_embalagem: TiposEmbalagem = TiposEmbalagem(name=input("::\tName: "))

    async with create_session() as db_handler:
        db_handler.add(tipos_embalagem)
        await db_handler.commit()

        return tipos_embalagem


async def insert_tipos_picole() -> TiposPicole:
    # Insert data in `Tipos Picole`

    print('** Insert Data in Table `Tipos Picole` **')

    tipos_picole: TiposPicole = TiposPicole(name=input("::\tNome:  "))
    async with create_session() as db_handler:
        db_handler.add(tipos_picole)
        await db_handler.commit()
        return tipos_picole


async def insert_ingredientes() -> Ingredientes:
    # Insert data in Table `Ingredientes`

    print("** Cadastrando Ingrediente **")

    ingrediente: Ingredientes = Ingredientes(name=input("::\tNome:  "))

    async with create_session() as db_handler:

        db_handler.add(ingrediente)
        await db_handler.commit()
        return ingrediente


async def insert_conservantes() -> Conservantes:
    # insert data in Table `Conservantes`
    print("Insert data in Table `Conservantes` **")
    conservante: Conservantes = Conservantes(name=input("::\tNome:  "), descricao=input("::\tDescricao:  "))
    async with create_session() as db_handler:
        db_handler.add(conservante)
        await db_handler.commit()
        return conservante


async def insert_revendedores() -> Revendedores:
    # Insert data in `Revendedores`

    print("Insert data in Table `Revendedores` **")

    revendedor: Revendedores = Revendedores(cnpj=input('::\tCNPJ:  '),
                                            razao_social=input("::\tRazao Social:  "),
                                            contato=input("::\tContato:  "))

    async with create_session() as db_handler:
        db_handler.add(revendedor)
        await db_handler.commit()
        return revendedor


async def insert_lotes() -> Lotes:
    # Insert data in Table `Lotes`
    print("Insert Data in Tables `Lotes` **")

    async with create_session() as db_handler:

        lote: Lotes = Lotes(id_tipos_picole=int(input("::\tID Tipo Picole: ")),
                            quantidade=int(input("\n::\tQuantidade:  ")))
        db_handler.add(lote)
        await db_handler.commit()
        await db_handler.refresh(lote)
        return lote


async def insert_notas_fiscais() -> NotasFiscais:
    # Insert data in table `Notas Fiscais`
    print("** Insert data in Table `Notas Fiscais` **")
    # Para teste vamos cadastrar um novo revendedor dentro deste método

    async with create_session() as db_handler:
        revendedor = await db_handler.scalar(select(Revendedores).where(Revendedores.id == int(input("::\tID Revendedor: "))))
        lote = await db_handler.scalar(select(Lotes).where(Lotes.id == int(input("::\tID Lote: "))))
        valor: float = float(input("::\tValor :"))
        nota_fiscal: NotasFiscais = NotasFiscais(id_revendedor=revendedor.id, valor=valor,
                                                 numero_serie=input("::\tNumero de Serie:  "),
                                                 descricao=input("::\tDescricao:  "))

        nota_fiscal.lote_association.append(LotesNotasFiscais(lote=lote))
        db_handler.add(nota_fiscal)
        await db_handler.commit()
        await db_handler.refresh(nota_fiscal)
        return nota_fiscal


async def insert_picoles() -> Picoles:
    # Insert data in `Picole`

    print("***\tCadastrando Picoles\t***")

    async with create_session() as db_handler:

        ingrediente = await db_handler.scalar(select(Ingredientes).where(Ingredientes.id == int(input("::\tID Ingrediente: "))))

        conservante = await db_handler.scalar(select(Conservantes).where(Conservantes.id == int(input("::\tID Conservante: "))))

        aditivo_nutritivo = await db_handler.scalar(select(AditivoNutritivo).where(AditivoNutritivo.id == int(input("::\tID Aditivo Nutritivo: "))))

        picole: Picoles = Picoles(valor=float(input("::\tValor: ")),
                                  id_sabor=int(input("::\tID Sabor: ")),
                                  id_tipo_embalagem=int(input("::\tID Tipo Embalagem")),
                                  id_tipos_picole=int(input("::\tID Tipo Picole")))

        picole.aditivo_nutritivo_association.append(AditivoNutritivoPicoles(aditivos_nutritivos=aditivo_nutritivo))
        picole.conservantes_association.append(ConservantesPicoles(conservantes=conservante))
        picole.ingredientes_association.append(IngredientesPicoles(ingredientes=ingrediente))
        db_handler.add(picole)

        await db_handler.commit()
        await db_handler.refresh(picole)
        return picole


if __name__ == '__main__':

    # 1 -- Tests Async Insert data `Aditivos Nutritivos` >> OK
    #asyncio.run(insert_aditivos_nutritivos())

    # 2 -- Tests Async insertt Data `Sabores` >> OK
    #asyncio.run(insert_sabores())

    # 3 -- Tests Async insert data `Tipos Embalagems` >> OK
    #asyncio.run(insert_tipos_embalagems())

    # 4 -- Tests Async insert data `Tipos Picoles` >> OK
    #asyncio.run(insert_tipos_picole())

    # 5 -- Tests Async insert data `Ingredientes` >> OK
    #asyncio.run(insert_ingredientes())

    # 6 -- Tests Async insert data `Conservantes` >> OK
    #asyncio.run(insert_conservantes())

    # 7 -- Tests Async insert data `Revendedores` >> OK
    #asyncio.run(insert_revendedores())

    # 8 -- Tests Async insert data `Lotes` >> ...
    #asyncio.run(insert_lotes())

    # 9 -- Tests Async Insert data `Notas Fiscais`
    #asyncio.run(insert_notas_fiscais())

    # 10 -- Tests Async Insert data `Picoles`
    #asyncio.run(insert_picoles())

    execucao = asyncio.get_event_loop()
    grupo = asyncio.gather(insert_aditivos_nutritivos(),
                           insert_sabores(),
                           insert_tipos_embalagems(),
                           insert_tipos_picole(),
                           insert_ingredientes(),
                           insert_conservantes(),
                           insert_revendedores(),
                           insert_lotes(),
                           insert_notas_fiscais(),
                           insert_picoles())
    execucao.run_until_complete(grupo)
    pendente = asyncio.all_tasks(loop=execucao)
    for task in pendente:
        task.cancel()
