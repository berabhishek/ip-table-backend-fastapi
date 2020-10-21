from sqlalchemy.orm import Session

from . import models, schemas

def create_region(db: Session, region: schemas.RegionCreate):
    db_item = models.Region(**region.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_region(db: Session):
    return db.query(models.Region).all()

def create_country(db: Session, country: schemas.CountryCreate):
    db_item = models.Country(**country.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_country(region: str, db: Session):
    return db.query(models.Country).filter(models.Country.region == region).all()

def create_city(db:Session, city: schemas.CityCreate):
    db_item = models.City(**city.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_city(country: str, db: Session):
    return db.query(models.City).filter(models.City.country == country).all()

def create_facility(db: Session, facility: schemas.FacilityCreate):
    db_item = models.Facility(**facility.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_facility(city: str, db: Session):
    return db.query(models.Facility).filter(models.Facility.city == city).all()

def create_connection(db: Session, connection: schemas.ConnectionCreate):
    db_item = models.Connection(**connection.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_connection(db: Session):
    return db.query(models.Connection).all()

def create_device1(db: Session, device1: schemas.Device1Create):
    db_item = models.Device1(**device1.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_device1(connection:str, db: Session):
    return db.query(models.Device1).filter(models.Device1.connection==connection).all()

def create_device2(db: Session, device2: schemas.Device2Create):
    db_item = models.Device2(**device2.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_device2(connection:str, db: Session):
    return db.query(models.Device2).filter(models.Device2.connection==connection).all()