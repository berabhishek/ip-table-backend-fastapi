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

def get_country(db: Session):
    return db.query(models.Country).filters(models.Country.region == region).all()

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