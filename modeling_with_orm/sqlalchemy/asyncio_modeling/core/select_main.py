from sqlalchemy.future import select

import asyncio
from typing import List

# Tables how objects
from models.sabores import Sabores
from models.aditivos_nutritivos import AditivoNutritivo
from models.revendedores import Revendedores
from models.picoles import Picoles

from utils.db_session import create_session
from utils.helper import data_para_string


async def select_aditivo_nutritivo() -> None:
    async with create_session() as handler:
        print("***\tInformacoes Tabela Aditivos Nutritivos\t***")
        #  Buscando
        query = select(AditivoNutritivo)
        aditivo_nutritivo: List[AditivoNutritivo] = await handler.execute(query)
        aditivo_nutritivo = aditivo_nutritivo.scalars().all()


async def select_main() -> None:

    await select_aditivo_nutritivo()


if __name__ == '__main__':
    # Tests selects:
    asyncio.run(select_main())
