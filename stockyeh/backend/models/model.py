from sqlalchemy.orm import DeclarativeBase


class MappedBase(DeclarativeBase):

    # table names
    __abstract__ = True
