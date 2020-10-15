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



   

