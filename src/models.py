import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)


    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__="planet"

    id = Column(Integer, primary_key=True)
    name=Column(String(200))
    population=Column(Integer)
    weather=Column(String(50), nullable=False)
    species = Column(String(100))
    homeworld = Column(String(200))


class People(Base):
    __tablename__="people"

    id = Column(Integer, primary_key=True)
    name=Column(String(200))
    age=Column(Integer)
    zodiac=Column(String(100))


class Favorite(Base):
    __tablename__="favorite"

    id=Column(Integer, primary_key=True)
    people_id=Column(Integer, ForeignKey('people.id'))
    people = relationship(People)


    user_id=Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    planet_id=Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
