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
from models.lotes import Lotes
from models.revendedores import Revendedores
from models.notas_fiscais import NotasFiscais
from models.picoles import Picoles


async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print("***\tInserindo dados na Tabela Aditivo Nutritivo\t***")
    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=input("::\tNome: "),
                                                           formula_quimica=input("::\tFormula Quimica: "))
    async with create_session() as handler:
        handler.add(aditivo_nutritivo)
        await handler.commit()
        return aditivo_nutritivo


async def insert_sabores() -> Sabores:

    print("***\tInserindo dados na Tabela Sabores\t***")
    sabores: Sabores = Sabores(nome=input("::\tNome: "))
    async with create_session() as handler:
        handler.add(sabores)
        await handler.commit()
        return sabores


async def insert_tipos_embalagems() -> TiposEmbalagem:
    print("***\tInserindo Dados na Tabela Tipos Embalagem\t***")
    tipos_embalagem: TiposPicole = TiposEmbalagem(nome=input("::\tNome: "))

    async with create_session() as handler:
        handler.add(tipos_embalagem)
        await handler.commit()
        return tipos_embalagem


async def insert_tipos_picole() -> TiposPicole:
    print("***\tInserindo Dados na Tabela Tipos Picole\t***")
    tipos_picole: TiposPicole = TiposPicole(nome=input("::\tNome: "))

    async with create_session() as handler:
        handler.add(tipos_picole)
        await handler.commit()
        return tipos_picole


async def insert_ingredientes() -> Ingredientes:
    print("***\tInserindo Dados na Tabela Ingredientes\t***")
    ingredientes: Ingredientes = Ingredientes(nome=input("::\tNome: "))

    async with create_session() as handler:
        handler.add(ingredientes)
        await handler.commit()
        return ingredientes


async def insert_conservantes() -> Conservantes:
    print("***\tInserindo Dados na Tabela Conservantes\t***")
    conservantes: Conservantes = Conservantes(nome=input("::\tNome: "), descricao=input("::\tDescricao: "))

    async with create_session() as handler:
        handler.add(conservantes)
        await handler.commit()
        return conservantes


async def insert_lotes() -> Lotes:
    print("***\tInserindo Dados na Tabela Lotes\t***")

    id_tipos_picole: int = int(input("::\tID Tipo Picole: "))
    quantidade: int = int(input("::\tQuantidade: "))

    lotes: Lotes = Lotes(id_tipos_picole=id_tipos_picole,
                         quantidade=quantidade)

    async with create_session() as handler:
        handler.add(lotes)
        await handler.commit()
        return lotes

async def insert_revendedores() -> Revendedores:
    print("***\tInserindo Dados na Tabela Revendedores\t***")

    revendedor: Revendedores = Revendedores(cnpj=input("::\tCNPJ: "),
                                            razao_social=input("::\tRazão Social: "),
                                            contato=input("::\tContato: "))
    async with create_session() as handler:
        handler.add(revendedor)
        await handler.commit()
        return revendedor


async def insert_notas_fiscais() -> NotasFiscais:
    print("***\tInserindo Dados na Tabelela Notas fiscais\t***")
    nota_fiscal: NotasFiscais = NotasFiscais(valor=float(input("::\tValor Nota Fiscal:")),
                                             numero_serie=input("::\tNumero de Serie: "),
                                             descricao=input("::\tDescricao: "),
                                             id_revendedor=int(input("::\tID Revendedor: ")))

    async with create_session() as handler:
        lote: Lotes = await handler.scalar(select(Lotes).where(Lotes.id == int(input("::\tID Lote: "))))
        nota_fiscal.lotes.append(lote)
        handler.add(nota_fiscal)
        await handler.commit()
        await handler.refresh(nota_fiscal)
        return nota_fiscal


async def insert_picoles() -> Picoles:
    print("***\tInserindo Dados na Tabela Picoles\t***")

    picole: Picoles = Picoles(preco=float(input("::\tPreco Picole: ")),
                              id_sabor=int(input("::\tID Sabor: ")),
                              id_tipos_picole=int(input("::\tID Tipo Picole: ")),
                              id_tipos_embalagem=int(input("::\tID Tipo Embalagem: ")))

    async with create_session() as handler:
        ingrediente: Ingredientes = await handler.scalar(select(Ingredientes).where(Ingredientes.id == int(input("::\tID Ingrediente: "))))
        picole.ingrediente.append(ingrediente)

        conservante: Conservantes = await handler.scalar(select(Conservantes).where(Conservantes.id == int(input("::\tID Conservante: "))))
        picole.conservante.append(conservante)

        aditivo_nutritivo: AditivoNutritivo = await handler.scalar(select(AditivoNutritivo).where(AditivoNutritivo.id == int(input("::\tID Aditivo Nutritivo: "))))
        picole.aditivo_nutritivo.append(aditivo_nutritivo)

        handler.add(picole)
        await handler.commit()
        await handler.refresh(picole)

        return picole


if __name__ == '__main__':

    # 1 -- Tests Async Insert data `Aditivos Nutritivos` >> OK
    #asyncio.run(insert_aditivo_nutritivo())

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

    # 8 -- Tests Async insert data `Lotes` >> OK
    #asyncio.run(insert_lotes())

    # 9 -- Tests Async Insert data `Notas Fiscais` >> OK
    #asyncio.run(insert_notas_fiscais())

    # 10 -- Tests Async Insert data `Picoles` >> OK
    #asyncio.run(insert_picoles())

    # 11 -- Tests running tasks in group >> `OK`
    execucao = asyncio.get_event_loop()  # Start handler

    # Create Group tasks
    grupo = asyncio.gather(insert_aditivo_nutritivo(),
                           insert_sabores(),
                           insert_tipos_embalagems(),
                           insert_tipos_picole(),
                           insert_ingredientes(),
                           insert_conservantes(),
                           insert_revendedores(),
                           insert_lotes(),
                           insert_notas_fiscais(),
                           insert_picoles())

    execucao.run_until_complete(grupo)  # Begin running with group over the handler
    pendente = asyncio.all_tasks(loop=execucao)  # Insert group tasks to asyncio loop

    # Iterable in group tasks to begin task
    for tarefa in pendente:
        execucao.run_until_complete(tarefa)  # Run One task
        tarefa.cancel()  # Finish Task
        execucao.close()  # Close handler
