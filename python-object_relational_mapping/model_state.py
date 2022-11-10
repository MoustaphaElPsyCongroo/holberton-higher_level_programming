#!/usr/bin/python3
"Class definition of a State and instance, using SQLAlchemy"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(
    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa', echo=True)
Base = declarative_base()


class State(Base):
    "State table model"
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
