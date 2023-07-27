import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine

from typing import Optional
from pathlib import Path

from utils.model_base import Base

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if __engine:
        # Se já existir uma `engine` continuar ...
        return

    if sqlite:  # Settings database `SQLite`
        file_db = "db/picoles.sqlite"  # Path to db this sqlite
        path_db = Path(file_db).parent  # Create file in root folder
        path_db.mkdir(parents=True,  # In folder root
                      exist_ok=True)  # If exists don't create
         #  Create Engine

        str_engine = f"sqlite+pysqlite:///{file_db}"
        __engine = sa.create_engine(url=str_engine,
                                    echo=False,
                                    connect_args={"check_same_thread": False}  # the `sqlite` don't thread in system
                                    )

    else:  # Settings to `PostgreSql`
        __engine = sa.create_engine(url="postgresql://postgres:Acesso93#@localhost:5432",
                                    echo=False
                                    )
    return __engine


def create_session():
    global __engine

    if not __engine:
        # To `sqlite` db add parameter `sqlite=True`
        create_engine()

    __session = sessionmaker(__engine,
                             expire_on_commit=False,
                             class_=Session)

    session: Session = __session()
    return session


def create_tables() -> Session:

    global __engine
    if not __engine:
        # To `sqlite` db add parameter `sqlite=True`
        create_engine()

    import __all_models
    Base.metadata.drop_all(__engine)
    Base.metadata.create_all(__engine)


if __name__ == '__main__':
    #  create_engine()  # `OK`
    #  create_session()  # `ok`
    #  create_tables()  # `ok`
    ...
