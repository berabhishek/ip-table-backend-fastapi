from typing import List, Optional

from pydantic import BaseModel

class CountryBase(BaseModel):
    name:str

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