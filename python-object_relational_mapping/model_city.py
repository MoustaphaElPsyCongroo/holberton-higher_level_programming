#!/usr/bin/python3
"Class definition of a State and instance, using SQLAlchemy"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State

engine = create_engine(
    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa', echo=True)
Base = declarative_base()


class City(Base):
    "City table model"
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))


if __name__ == "__main__":
    State.cities = relationship("City")
    Base.metadata.create_all(engine)
