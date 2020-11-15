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

class Asnumber(Base):
    __tablename__="asnumber"

    name = Column(String, primary_key=True)

    facility = Column(String, ForeignKey("facility.name"))

class Vlan(Base):
    __tablename__="vlan"

    vlanmin = Column(Integer)
    vlanmax = Column(Integer)
    id = Column(Integer, primary_key=True, index=True)

    facility = Column(String, ForeignKey("facility.name"))

class Parentsubnet(Base):
    __tablename__="parentsubnet"

    parentsubnet = Column(String, primary_key=True)

    facility = Column(String, ForeignKey("facility.name"))

class Subnet(Base):
    __tablename__="subnet"

    childsubnet = Column(String, primary_key=True)

    parentsubnet = Column(String, ForeignKey("parentsubnet.parentsubnet"))


class Project(Base):
    __tablename__="project"

    id = Column(Integer, primary_key=True, index=True)
    projectid = Column(String)
    projectname = Column(String)
    vrfname = Column(String)
    facility = Column(String, ForeignKey("facility.name"))
   
class Connect(Base):
    __tablename__="connect"

    id = Column(Integer, primary_key=True, index=True)
    vlan = Column(Integer, unique=True)
    childsubnet = Column(String, ForeignKey("subnet.childsubnet"))
    device1 = Column(String, ForeignKey("device1.name"))
    device2 = Column(String, ForeignKey("device2.name"))

class Iptable(Base):
    __tablename__="iptable"

    id = Column(Integer, primary_key=True, index=True)
    projectid = Column(String, ForeignKey("project.projectid"))
    connection = Column(String)
    connect1 = Column(Integer, ForeignKey("connect.id"), nullable=True)
    connect2 = Column(Integer, ForeignKey("connect.id"), nullable=True)
    connect3 = Column(Integer, ForeignKey("connect.id"), nullable=True)
    connect4 = Column(Integer, ForeignKey("connect.id"), nullable=True)