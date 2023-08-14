import asyncio

from utils.db_session import create_tables

if __name__ == '__main__':
    execucao = asyncio.get_event_loop()
    execucao.run_until_complete(create_tables())
