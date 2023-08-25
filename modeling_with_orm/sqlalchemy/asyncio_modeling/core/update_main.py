from sqlalchemy.future import select

import asyncio

from utils.db_session import create_session

from models.aditivos_nutritivos import AditivoNutritivo
from models.sabores import Sabores

async def update_aditivo_nutritivo() -> None:
    print("***\tAtualizar Tabela Aditivos Nutritivos\t***")
    async with create_session() as handler, handler.begin():
        aditivo_nutritivo: AditivoNutritivo = await handler.scalar(select(AditivoNutritivo).where(AditivoNutritivo.id == int(input("::\tBuscar Por ID: "))))
        print("***\tAtualizar Dados\t***")
        aditivo_nutritivo.nome = input("::\tNOME: ")
        aditivo_nutritivo.formula_quimica = input("::\tFORMULA QUIMICA: ")


async def update_sabores() -> None:
    print("\n\n***\tAtualizar Tabela Sabores\t***")
    async with create_session() as handler, handler.begin():
        sabor: Sabores = await handler.scalar(select(Sabores).where(Sabores.id == int(input("::\tBuscar Por ID: "))))
        print("***\tAtualizar Dados\t***")
        sabor.nome: str = input("::\tNOME: ")


def update_main() -> None:
    maker = asyncio.get_event_loop()

    maker.run_until_complete(update_aditivo_nutritivo())
    maker.run_until_complete(update_sabores())



if __name__ == '__main__':
    # Tests updates
    update_main()
