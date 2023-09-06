from sqlalchemy.orm import sessionmaker
# Import Class to engines and sessions async from SqlAlchemy
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession, create_async_engine)

from typing import Optional
from pathlib import Path

from utils.model_base import Base

__engine: Optional[AsyncEngine] = None


def create_engine(sqlite: bool = False) -> AsyncEngine:
    global __engine

    if __engine:
        # Se já existir uma `engine` continuar ...
        return

    if sqlite:  # Settings database `SQLite`
        file_db = "db/picoles.  sqlite"  # Path to db this sqlite
        path_db = Path(file_db).parent  # Create file in root folder
        path_db.mkdir(parents=True,  # In folder root
                      exist_ok=True)  # If exists don't create

        #  Create Engine
        __engine = create_async_engine(url=f"sqlite+aiosqlite:///{file_db}",  # String engine
                                       echo=False,  # Nice output LOGs
                                       connect_args={"check_same_thread": False})  # SQLite not support thread

    else:  # Settings to `PostgreSql`
        __engine = create_async_engine(url="postgresql+asyncpg://postgres:Acesso93#@localhost:5432", echo=False)
    return __engine


def create_session() -> AsyncSession:
    global __engine

    if not __engine:
        # To `sqlite` db add parameter `sqlite=True`
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=AsyncSession)
    session: AsyncSession = __session()
    return session


async def create_tables() -> None:
    #  To behaviours `async` create functions async where content a by `await` over the statements manager

    global __engine
    if not __engine:
        # To `sqlite` db add parameter `sqlite=True`
        create_engine()

    import __all_models
    async with __engine.begin() as conn:
        # Statement manager async
        await conn.run_sync(Base.metadata.drop_all)  # To send
        await conn.run_sync(Base.metadata.create_all)  # To send


if __name__ == '__main__':
    #  create_engine()  # `OK`
    #  create_session()  # `OK`
    #  create_tables()  # `OK`
    ...