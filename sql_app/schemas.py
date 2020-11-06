from typing import List, Optional

from pydantic import BaseModel


class RegionBase(BaseModel):
    name:str

class RegionCreate(RegionBase):
    pass

class Region(RegionBase):
    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    name:str
    region:str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    class Config:
        orm_mode = True

class CityBase(BaseModel):
    name: str
    country: str

class CityCreate(CityBase):
    pass

class City(CityBase):
    class Config:
        orm_mode = True

class FacilityBase(BaseModel):
    name: str
    city: str

class FacilityCreate(FacilityBase):
    pass

class Facility(FacilityBase):
    class Config:
        orm_mode = True


class ConnectionBase(BaseModel):
    name: str

class ConnectionCreate(ConnectionBase):
    pass

class Connection(ConnectionBase):
    class Config:
        orm_mode = True

class Device1Base(BaseModel):
    name : str
    connection : str

class Device1Create(Device1Base):
    pass

class Device1(Device1Base):
    class Config:
        orm_mode = True

class Device2Base(BaseModel):
    name : str
    connection : str

class Device2Create(Device2Base):
    pass

class Device2(Device2Base):
    class Config:
        orm_mode = True

class AsnumberBase(BaseModel):
    name : str
    facility : str

class AsnumberCreate(AsnumberBase):
    pass

class Asnumber(AsnumberBase):
    class Config:
        orm_mode = True

class VlanBase(BaseModel):
    facility : str
    vlanmin : int
    vlanmax : int

class VlanCreate(VlanBase):
    pass

class Vlan(VlanBase):
    class Config:
        orm_mode = True

class ParentsubnetBase(BaseModel):
    parentsubnet : str
    facility : str
    

class ParentsubnetCreate(ParentsubnetBase):
    pass

class Parentsubnet(ParentsubnetBase):
    class Config:
        orm_mode = True

class SubnetBase(BaseModel):
    childsubnet : str
    parentsubnet : str

class SubnetCreate(SubnetBase):
    pass

class Subnet(SubnetBase):
    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    projectid : str
    projectname : str
    vrfname : str
    facility : str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    class Config:
        orm_mode = True


class ConnectBase(BaseModel):
    vlan : int
    childsubnet : str
    device1 : str
    device2 : str

class ConnectCreate(ConnectBase):
    pass

class Connect(ConnectBase):
    id : int
    class Config:
        orm_mode = True

class IptableBase(BaseModel):
    projectid : str
    connection : str
    connect1 : int
    connect2 : int
    connect3 : int 
    connect4 : int

class IptableCreate(IptableBase):
    pass

class Iptable(IptableBase):
    id : int
    class Config:
        orm_mode = True
