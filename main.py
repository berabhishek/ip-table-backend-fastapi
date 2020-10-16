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

@app.get("/formhelper/region{region}", response_model =List[schemas.Region])
def get_region(db: Session = Depends(get_db)):
    return crud.get_region(db=db)


@app.post("/formhelper/country", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)

@app.get("/formhelper/country", response_model =List[schemas.Country])
def get_country(db: Session = Depends(get_db)):
    return crud.get_country(db=db)

@app.get("/formhelper/city/{city}", response_model=List[schemas.City])
def get_city_name(city: str, db: Session = Depends(get_db)):
    return crud.get_city(city, db=db)

@app.post("/formhelper/city", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db=db, city=city)

@app.get("/formhelper/state/{country}")
def get_city_name(country: str, db: Session = Depends(get_db)):
    return crud.get_city(country, db=db)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3030)

#blabla