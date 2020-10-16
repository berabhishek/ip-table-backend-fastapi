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