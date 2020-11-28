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

@app.get("/formhelper/region", response_model =List[schemas.Region])
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

@app.get("/formhelper/city/{country}", response_model =List[schemas.City])
def get_city_name(country: str, db: Session = Depends(get_db)):
    return crud.get_city(country, db=db)

@app.get("/formhelper/vrfname")
def get_vrf_name(db:Session = Depends(get_db)):
    return crud.get_vrfnames(db=db)

@app.post("/formhelper/facility", response_model=schemas.Facility)
def create_facility(facility: schemas.FacilityCreate, db: Session = Depends(get_db)):
    return crud.create_facility(db=db, facility=facility)

@app.get("/formhelper/facility/{city}", response_model =List[schemas.Facility])
def get_facility_name(city: str, db: Session = Depends(get_db)):
    return crud.get_facility(city, db=db)

@app.post("/formhelper/connection", response_model=schemas.Connection)
def create_connection(connection: schemas.ConnectionCreate, db: Session = Depends(get_db)):
    return crud.create_connection(db=db, connection=connection)

@app.get("/formhelper/connection", response_model =List[schemas.Connection])
def get_connection_name(db: Session = Depends(get_db)):
    return crud.get_connection(db=db)

@app.post("/formhelper/device1", response_model=schemas.Device1)
def create_device1(device1: schemas.Device1Create, db: Session = Depends(get_db)):
    return crud.create_device1(db=db, device1 = device1)

@app.get("/formhelper/device1/{connection}", response_model =List[schemas.Device1])
def get_device1(connection: str, db: Session = Depends(get_db)):
    return crud.get_device1(connection, db=db)

@app.post("/formhelper/device2", response_model=schemas.Device2)
def create_device2(device2: schemas.Device2Create, db: Session = Depends(get_db)):
    return crud.create_device2(db=db, device2 = device2)

@app.get("/formhelper/device2/{connection}", response_model =List[schemas.Device2])
def get_device2(connection: str, db: Session = Depends(get_db)):
    return crud.get_device2(connection, db=db)

@app.post("/formhelper/asnumber", response_model=schemas.Asnumber)
def create_asnumber(asnumber: schemas.AsnumberCreate, db: Session = Depends(get_db)):
    return crud.create_asnumber(db=db, asnumber = asnumber)

@app.get("/formhelper/asnumber/{facility}", response_model =List[schemas.Asnumber])
def get_asnumber(facility: str, db: Session = Depends(get_db)):
    return crud.get_asnumber(facility, db=db)

@app.post("/formhelper/vlan", response_model=schemas.Vlan)
def create_vlan(vlan: schemas.VlanCreate, db: Session = Depends(get_db)):
    return crud.create_vlan(db=db, vlan = vlan)

@app.get("/formhelper/vlan/{facility}", response_model =List[schemas.Vlan])
def get_vlan(facility: str, db: Session = Depends(get_db)):
    return crud.get_vlan(facility, db=db)

@app.post("/formhelper/parentsubnet", response_model=schemas.Parentsubnet)
def create_parentsubnet(parentsubnet: schemas.ParentsubnetCreate, db: Session = Depends(get_db)):
    return crud.create_parentsubnet(db=db, parentsubnet = parentsubnet)

@app.get("/formhelper/parentsubnet/{facility}", response_model =schemas.Parentsubnet)
def get_parentsubnet(facility: str, db: Session = Depends(get_db)):
    return crud.get_parentsubnet(facility, db=db)

@app.post("/formhelper/subnet", response_model=schemas.Subnet)
def create_subnet(subnet: schemas.SubnetCreate, db: Session = Depends(get_db)):
    return crud.create_subnet(db=db, subnet = subnet)

@app.get("/formhelper/subnet/{parentsubnet}/{entervalue}", response_model =List[schemas.Subnet])
def get_subnet(parentsubnet: str, entervalue: str, db: Session = Depends(get_db)):
    return crud.get_subnet(parentsubnet , entervalue, db=db)

@app.post("/formhelper/project", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project = project)

@app.post("/formhelper/setipdata/existing")
def create_projectipdata(projectipdata: dict, db: Session = Depends(get_db)):
    return crud.create_projectipdata(db=db, projectipdata = projectipdata)

@app.get("/formhelper/get_free_vlans/{facility}")
def get_vlans(facility: str, db: Session = Depends(get_db)):
    return crud.get_free_vlan(facility, db=db)

@app.get("/formhelper/validate/{projectname}/{projectid}/{vrfname}")
def get_project(projectname: str, projectid: str, vrfname: str, db:Session = Depends(get_db)):
    return crud.check_project_validity(projectname, projectid, vrfname, db=db)

@app.post("/formhelper/connect", response_model=schemas.Connect)
def create_connect(connect: schemas.ConnectCreate, db: Session = Depends(get_db)):
    return crud.create_connect(db=db, connect = connect)

@app.get("/formhelper/connect/{id}",response_model = schemas.Connect)
def get_connect(id: int, db: Session = Depends(get_db)):
    return crud.get_connect(id, db=db)

@app.get("/formhelper/iptable/{id}",response_model = schemas.Iptable)
def get_iptable(id: int, db: Session = Depends(get_db)):
    return crud.get_iptable(id, db=db)

@app.get("/all")
def get_all_someting(db: Session = Depends(get_db)):
    return crud.get_all_connect(db)

@app.get("/formhelper/alldata/{id}")
def get_output_data(id: int, db: Session = Depends(get_db)):
    return crud.get_output_data(id, db = db)

@app.delete("/formhelper/iptable/{id}")
def delete_iptable(id: int, db: Session = Depends(get_db)):
    return crud.delete_iptable(id, db = db)

@app.delete("/formhelper/cleariptable/{projectname}/{projectid}/{vrfname}/{facility}")
def delete_project_id(projectname: str, projectid: str, vrfname: str, facility: str, db: Session = Depends(get_db)):
    return crud.delete_project_id(projectname, projectid, vrfname, facility, db = db)

@app.get("/formhelper/subnetfilter/{facility}/{entervalue}")
def get_subnet_filtered(facility: str, entervalue: int, db: Session = Depends(get_db)):
    return crud.get_subnet_filtered(facility, entervalue, db=db)

@app.get("/formhelper/getconnect/{projectname}/{projectid}/{vrfname}/{facility}")
def get_existing_connections(projectname: str, projectid: str, vrfname: str, facility: str, db: Session = Depends(get_db)):
    return crud.get_existing_connections(projectname, projectid, vrfname, facility, db)

"""Start all the internal endpoints with internals start case """

#this endpoint must be restricted to development
@app.delete("/internals/clearconnection")
def delete_all_connections(db: Session = Depends(get_db)):
    return crud.delete_all_connections(db=db)

@app.delete("/internals/cleariptable")
def delete_all_connections(db: Session = Depends(get_db)):
    return crud.delete_all_iptables(db=db)
if __name__ == "__main__":
    uvicorn.run(app, port=3030)