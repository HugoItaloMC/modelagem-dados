from sqlalchemy import select
from sqlalchemy.orm import joinedload, join
from sqlalchemy import ScalarResult

import asyncio
import json
from typing import List, Coroutine, AsyncIterable

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
        print(" ".join(map(str, await handler.scalars(select(AditivoNutritivo).where(AditivoNutritivo.id == int(input("::\tBuscar por ID: ")))))))


async def select_sabores() -> None:
    print("\n\n***\tInformacões Tabela Sabores\t***")
    async with create_session() as handler:
        print("\n".join(map(str, await handler.scalars(select(Sabores).order_by(Sabores.nome)))))


async def select_tipos_embalagem() -> None:
    print("\n\n***Informacões da Tabela Tipos Embalagem\t***")
    async with create_session() as handler:
        print("\n".join(map(str, await handler.scalars(select(TiposEmbalagem).where(TiposEmbalagem.id == int(input("::\tBuscar ID Tipos Embalagem\nID: ")))))))


async def select_tipos_picole() -> None:
    print("\n\n***\tInformacões Tabela Tipos Picole\t***")
    async with create_session() as handler:
        tipo_picole: TiposPicole = await handler.scalar(select(TiposPicole).where(TiposPicole.id == int(input("::\tBuscar ID Tipo Picole\nID:\t"))))
        print(tipo_picole)


async def select_ingredientes() -> None:
    print("\n\n***\tinformacoes Tabela Ingredientes\t***")
    async with create_session() as handler:
        print(" ".join(map(str, await handler.scalar(select(Ingredientes).where(Ingredientes.id == int(input("::\tBuscar Por ID: ")))))))


async def select_conservantes() -> None:
    print("\n\n***\tinformacoes Tabela Conservantes\t***")
    async with create_session() as handler:
        print(" ".join(map(str, await handler.scalar(select(Conservantes).where(Conservantes.id == int(input("::\tBuscar Por ID: ")))))))


async def select_revendedores() -> None:
    print("\n\n***\tinformacoes Tabela Revendedores\t***")
    async with create_session() as handler:
        print(" ".join(map(str, await handler.scalar(select(Revendedores).where(Revendedores.id == int(input("::\tBuscar Por ID: ")))))
))


async def select_lotes() -> None:
    print("\n\n***\tinformacoes Tabela Lotes\t***")
    async with create_session() as handler:
        print("\n".join(map(repr, await handler.scalars(select(Lotes).select_from(join(Lotes, TiposPicole)).where(TiposPicole.id == int(input("::\tBuscar Lote por ID Tipo Picole\nID: ")))))))


async def select_notas_fiscais() -> None:
    print("\n\n***\tinformacoes Tabela Notas Fiscais\t***")
    async with (create_session() as handler):
        nota_fiscal: ScalarResult[NotasFiscais] = await handler.scalars(select(NotasFiscais))
        quantidade: int = int(input("::\tBuscar Nota Fiscal por Quantidade em Lote:\t"))
        print(" ".join(map(str, [line for line in nota_fiscal.unique().all() if any(lote.quantidade == quantidade for lote in line.lotes)]
)))


async def select_picoles_complex() -> None:
    print("\n\n***\tInformacoes de Tabela Picoles a partir de Relacionamentos\t***")
    handler = create_session()
    """
      Para recuperarmos informacões de relacionamentos complexos `N=N`,  devemos  primeiramente  iterar sobre o atributo 
    que representa  o  objeto  relacionado e assim aplicar os filtros de recuperacão que no caso  está sendo  comparacão  
    entre: `objeto.id == input_id_objeto`
    """
    async with handler:
        picoles: ScalarResult[Picoles] = await handler.scalars(select(Picoles))

        id_ingrediente: int = int(input("::\tBuscar Picole por ID Ingrediente\nID:\t"))
        print("\n".join(map(repr, [line for line in picoles.unique().all() if any(ingrediente.id == id_ingrediente for ingrediente in line.ingrediente)])))

    async with handler:
        picoles: ScalarResult[Picoles] = await handler.scalars(select(Picoles))

        id_conservante: int = int(input("::\tBuscar Picole por ID Conservante\nID:\t"))
        print("\n".join(map(repr, [line for line in picoles.unique().all() if any(conservante.id == id_conservante for conservante in line.conservante)])))

    async with handler:
        picoles: ScalarResult[Picoles] = await handler.scalars(select(Picoles))
        id_aditivo_nutritivo: int = int(input("::\tBuscar Picole por ID Aditivo Nutritivo\nID:\t"))
        print("\n".join(map(repr, [line for line in picoles.unique().all() if any(aditivo_nutritivo.id == id_aditivo_nutritivo for aditivo_nutritivo in line.aditivo_nutritivo)])))

    """
        Em relacionamentos  em  que  temos  o objeto sendo representado como coluna em uma chave estrangeira, fica mais 
    performático utilizar uma recuperacão utilizando operador `join`
    """
    async with handler:
        picoles: ScalarResult[Picoles] = await handler.scalars(select(Picoles).select_from(join(Picoles, Sabores)).where(Sabores.id == int(input("::\tBuscar Picole por ID Sabores\nID:\t"))))
        print(" ".join(map(repr, picoles.unique().all())))

    async with handler:
        picoles: ScalarResult[Picoles] = await handler.scalars(select(Picoles).select_from(join(Picoles, TiposEmbalagem)).where(TiposEmbalagem.id == int(input("::\tBuscar Picole por ID Tipo Embalagem\nID:\t"))))
        print(" ".join(map(repr, picoles.unique().all())))

    async with handler:
        picoles: ScalarResult[Picoles] = await handler.scalars(select(Picoles).select_from(join(Picoles, TiposPicole)).where(TiposPicole.id == int(input("::\tBuscar Picole por ID Tipo Picole\nID:\t"))))
        print(" ".join(map(repr, picoles.unique().all())))


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
    maker.run_until_complete(select_picoles_complex())


if __name__ == '__main__':
    # Tests selects:
    select_main()
