from typing import List
import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sql_app.database import SessionLocal, engine
from sql_app import crud, models, schemas

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/formhelper/region", response_model=schemas.Region)
def create_region(region: schemas.RegionCreate, db: Session = Depends(get_db)):
    return crud.create_region(db=db, region=region)

@app.get("/formhelper/region/{region}", response_model =List[schemas.Region])
def get_region(db: Session = Depends(get_db)):
    return crud.get_region(db=db)


@app.post("/formhelper/country", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)

@app.get("/formhelper/country/{region}", response_model =List[schemas.Country])
def get_country(region: str, db: Session = Depends(get_db)):
    return crud.get_country(region, db=db)

@app.post("/formhelper/city", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db=db, city=city)

@app.get("/formhelper/city/{country}")
def get_city_name(country: str, db: Session = Depends(get_db)):
    return crud.get_city(country, db=db)



@app.get("/formhelper/facility/{city}")
def get_facility_name(city: str, db: Session = Depends(get_db)):
    return crud.get_facility(city, db=db)

@app.post("/formhelper/facility", response_model=schemas.Facility)
def create_facility(facility: schemas.FacilityCreate, db: Session = Depends(get_db)):
    return crud.create_facility(db=db, facility=facility)

@app.post("/formhelper/connection", response_model=schemas.Connection)
def create_connection(connection: schemas.ConnectionCreate, db: Session = Depends(get_db)):
    return crud.create_connection(db=db, connection=connection)

@app.get("/formhelper/connection")
def get_connection_name(db: Session = Depends(get_db)):
    return crud.get_connection(db=db)

@app.post("/formhelper/device1", response_model=schemas.Device1)
def create_device1(device1: schemas.Device1Create, db: Session = Depends(get_db)):
    return crud.create_device1(db=db, device1 = device1)

@app.get("/formhelper/device1/{connection}")
def get_device1(connection: str, db: Session = Depends(get_db)):
    return crud.get_device1(connection, db=db)

@app.post("/formhelper/device2", response_model=schemas.Device2)
def create_device2(device2: schemas.Device2Create, db: Session = Depends(get_db)):
    return crud.create_device2(db=db, device2 = device2)

@app.get("/formhelper/device2/{connection}")
def get_device2(connection: str, db: Session = Depends(get_db)):
    return crud.get_device2(connection, db=db)


if __name__ == "__main__":
    uvicorn.run(app, port=3030)

#blabla