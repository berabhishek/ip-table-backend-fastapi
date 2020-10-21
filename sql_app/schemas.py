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