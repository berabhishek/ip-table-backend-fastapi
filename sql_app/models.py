from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Country(Base):
    __tablename__ = "country"

    name=Column(String, primary_key=True)

class City(Base):
    __tablename__ = "city"

    name = Column(String, primary_key=True)

    country = Column(String, ForeignKey("country.name"))