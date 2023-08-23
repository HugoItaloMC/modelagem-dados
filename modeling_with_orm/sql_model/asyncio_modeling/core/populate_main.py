# Módulo auxiliar para povoar o banco de dados `fabrica de picoles`

from tqdm import tqdm
from sqlalchemy import select
from sqlalchemy.orm import Session

import asyncio
from typing import Coroutine
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


# Functions to Populate Tables >>

# 1 -- Aditivos Nutritivos`


async def populate_aditivos_nutritivos() -> None:

    async with create_session() as handler:
        # The package `tqdm` create custom loading bar
        for n in tqdm(range(1, 101),  # Sized Loop
                      desc="Cadastrando Aditivo Nutritivo",  # Bar description
                      colour=string_hexadecimal()):  # Loading Bar Color

            handler.add(AditivoNutritivo(nome=gerar_string(), formula_quimica=gerar_string(frase=True)))

        await handler.commit()
        await handler.close()


# 2 -- `Sabores`


async def populate_sabores() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Cadastrando Sabores", colour=string_hexadecimal()):
            handler.add(Sabores(nome=gerar_string()))

        await handler.commit()
        await handler.close()


# 3 -- `Tipos Embalagem`


async def populate_tipos_embalagem() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Cadastrando Tipo Embalagem", colour=string_hexadecimal()):
            handler.add(TiposEmbalagem(nome=gerar_string()))

        await handler.commit()
        await handler.close()


# 4 -- `Tipos Picole`

async def populate_tipos_picole() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Cadastrando Tipos Picole...", colour=string_hexadecimal()):
            tipo_picole: TiposPicole = TiposPicole(nome=gerar_string())
            handler.add(tipo_picole)

        await handler.commit()
        await handler.close()
    await asyncio.sleep(0.01)


# 5 --  `Ingredientes`


async def populate_ingredientes() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Populando Tabela Ingredientes...", colour=string_hexadecimal()):
            handler.add(Ingredientes(nome=gerar_string()))

        await handler.commit()
        await handler.close()


# 6 -- `Conservantes`


async def populate_conservantes() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Populando Tabela Conservantes...", colour=string_hexadecimal()):
            handler.add(Conservantes(nome=gerar_string(), descricao=gerar_string(frase=True)))

        await handler.commit()
        await handler.close()


# 7 -- `Revendedores`


async def populate_revendedores() -> None:
    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Populando Tabela Revendedores...", colour=string_hexadecimal()):
            handler.add(Revendedores(cnpj=str(gerar_inteiros()),
                                     razao_social=gerar_string(frase=True),
                                     contato=gerar_string()))

        await handler.commit()
        await handler.close()

# 8 -- `Lotes`


async def populate_lotes() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Populando Tabela Lotes...", colour=string_hexadecimal()):
            handler.add(Lotes(id_tipos_picole=gerar_inteiros(), quantidade=gerar_inteiros()))

        await handler.commit()
        await handler.close()
    await asyncio.sleep(2.0)


# 9 -- `Notas Fiscais`


async def populate_notas_fiscais() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Populando Tabela Notas Fiscais...", colour=string_hexadecimal()):
            nota_fiscal: NotasFiscais = NotasFiscais(valor=gerar_float(digitios=3),
                                                     numero_serie=gerar_string(),
                                                     descricao=gerar_string(frase=True),
                                                     id_revendedor=gerar_inteiros())

            lote = await handler.scalar(select(Lotes).where(Lotes.id == gerar_inteiros()))
            nota_fiscal.lotes.append(lote)
            handler.add(nota_fiscal)

        await handler.commit()
        await handler.refresh(nota_fiscal)
        await handler.close()
    await asyncio.sleep(2.0)


# 10 -- `Picoles`


async def populate_picoles() -> None:

    async with create_session() as handler:
        for _ in tqdm(range(1, 101), desc="Populando Tabela Picoles...", colour=string_hexadecimal()):

            picoles: Picoles = Picoles(preco=gerar_float(),
                                       id_sabor=gerar_inteiros(),
                                       id_tipos_embalagem=gerar_inteiros(),
                                       id_tipos_picole=gerar_inteiros())

            ingrediente: Coroutine[Ingredientes] = await handler.scalar(select(Ingredientes)
                                                                        .where(Ingredientes.id == gerar_inteiros()))
            picoles.ingrediente.append(ingrediente)

            random_: float = gerar_float()
            if random_ > 4:
                aditivo_nutritivo: Coroutine[AditivoNutritivo] = await handler.scalar(select(AditivoNutritivo)
                                                                                      .where(AditivoNutritivo.id ==
                                                                                             gerar_inteiros()))
                picoles.aditivo_nutritivo.append(aditivo_nutritivo)

            else:
                conservante: Coroutine[Conservantes] = await handler.scalar(select(Conservantes)
                                                                            .where(Conservantes.id == gerar_inteiros()))
                picoles.conservante.append(conservante)

            handler.add(picoles)

        await handler.commit()
        await handler.refresh(picoles)
        await handler.close()
    await asyncio.sleep(2.0)


def populate_main() -> None:
    # Running Group Tasks >>
    maker = asyncio.get_event_loop()
    tasks_nice_group = asyncio.gather(populate_aditivos_nutritivos(),
                                      populate_sabores(),
                                      populate_tipos_embalagem(),
                                      populate_tipos_picole(),
                                      populate_ingredientes(),
                                      populate_conservantes(),
                                      populate_revendedores(),
                                      populate_lotes())
    maker.run_until_complete(tasks_nice_group)
    hanging = asyncio.all_tasks(loop=maker)
    for task in hanging:
        maker.run_until_complete(task)
        task.cancel()
        maker.close()

    # Complex Tasks lonely running
    maker.run_until_complete(populate_notas_fiscais())
    maker.run_until_complete(populate_picoles())


if __name__ == '__main__':

    # Run Populate
    # Tests Populates Tables >>
    populate_main()



