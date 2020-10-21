from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Region(Base):
    __tablename__ = "region"

    name =  Column(String, primary_key=True)

class Country(Base):
    __tablename__ = "country"

    name=Column(String, primary_key=True)

    region = Column(String, ForeignKey("region.name") )

class City(Base):
    __tablename__ = "city"

    name = Column(String, primary_key=True)

    country = Column(String, ForeignKey("country.name"))

class Facility(Base):
    __tablename__ = "facility"

    name = Column(String, primary_key=True)

    city = Column(String, ForeignKey("city.name"))

class Connection(Base):
    __tablename__ = "connection"

    name = Column(String, primary_key=True)

class Device1(Base):
    __tablename__= "device1"

    name = Column(String, primary_key=True)

    connection = Column(String, ForeignKey("connection.name"))

class Device2(Base):
    __tablename__= "device2"

    name = Column(String, primary_key=True)

    connection = Column(String, ForeignKey("connection.name"))

   

