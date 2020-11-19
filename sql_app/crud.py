from sqlalchemy.orm import Session

from . import models, schemas

def  insert_into_model(db: Session, row_object, model):
    try:
        row_object = row_object.dict()
    except:
        pass
    db_item = model(**row_object)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_free_vlan(facility: str, db: Session):
    min_max = db.query(models.Vlan).filter(models.Vlan.facility == facility).first()
    try:
        vmin = min_max.__dict__["vlanmin"]
        vmax = min_max.__dict__["vlanmax"]

        used = db.query(models.Connect).filter((models.Connect.vlan >= vmin)).filter((models.Connect.vlan <= vmax)).all()
        used_vlans = []
        for u in used:
            used_vlans.append(u.__dict__["vlan"])
        free_vlans = []
        for vlan in range(vmin, vmax+1):
            if len(free_vlans) == 4:
                return free_vlans
            if vlan not in used_vlans:
                free_vlans.append(vlan)
        return free_vlans
    except:
        return []

def get_vrfnames(db: Session):
    vrfnames = []
    for vrf in db.query(models.Project).all():
        vrfnames.append(vrf.__dict__["vrfname"])
    return vrfnames

def check_project_validity( projectname: str, projectid: str, vrfname: str, db: Session):
    pobj = models.Project
    project = db.query(pobj).filter(pobj.projectid == projectid).filter(pobj.projectname == projectname).filter(pobj.vrfname == vrfname).all()
    return {
        "valid": len(project) > 0
    }


def create_region(db: Session, region: schemas.RegionCreate):
    return insert_into_model(db, region, models.Region)

def get_region(db: Session):
    return db.query(models.Region).all()

def create_country(db: Session, country: schemas.CountryCreate):
    return insert_into_model(db, country, models.Country)

def get_country(region: str, db: Session):
    return db.query(models.Country).filter(models.Country.region == region).all()

def create_city(db:Session, city: schemas.CityCreate):
    return insert_into_model(db, city, models.City)

def get_city(country: str, db: Session):
    return db.query(models.City).filter(models.City.country == country).all()

def create_facility(db: Session, facility: schemas.FacilityCreate):
    return insert_into_model(db, facility, models.Facility)

def get_facility(city: str, db: Session):
    return db.query(models.Facility).filter(models.Facility.city == city).all()

def create_connection(db: Session, connection: schemas.ConnectionCreate):
    return insert_into_model(db, connection, models.Connection)

def get_connection(db: Session):
    return db.query(models.Connection).all()

def create_device1(db: Session, device1: schemas.Device1Create):
    return insert_into_model(db, device1, models.Device1)

def get_device1(connection:str, db: Session):
    return db.query(models.Device1).filter(models.Device1.connection==connection).all()

def create_device2(db: Session, device2: schemas.Device2Create):
    return insert_into_model(db, device2, models.Device2)

def get_device2(connection:str, db: Session):
    return db.query(models.Device2).filter(models.Device2.connection==connection).all()

def create_asnumber(db: Session, asnumber: schemas.AsnumberCreate):
    return insert_into_model(db, asnumber, models.Asnumber)

def get_asnumber(facility:str , db:Session):
    return db.query(models.Asnumber).filter(models.Asnumber.facility==facility).all()

def create_vlan(db: Session, vlan: schemas.VlanCreate):
    return insert_into_model(db, vlan, models.Vlan)

def get_vlan(facility:str , db:Session):
    return db.query(models.Vlan).filter(models.Vlan.facility==facility).all()

def create_parentsubnet(db: Session, parentsubnet: schemas.ParentsubnetCreate):
    return insert_into_model(db, parentsubnet, models.Parentsubnet)

def get_parentsubnet(facility:str , db:Session):
    return db.query(models.Parentsubnet).filter(models.Parentsubnet.facility==facility).first() 

def create_subnet(db: Session, subnet: schemas.SubnetCreate):
    return insert_into_model(db, subnet, models.Subnet)

def get_subnet(parentsubnet:str , entervalue: str, filterentervalue: int,  db:Session):
    parentsubnet += "/"+entervalue
    return db.query(models.Subnet).filter(models.Subnet.parentsubnet==parentsubnet).filter(models.Subnet.childsubnet.endswith("/"+str(filterentervalue))).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    return insert_into_model(db, project, models.Project)

def create_projectipdata(db: Session, projectipdata: dict):
    connectids = []
    for i in range(1, 5):
        istr = str(i)
        if(projectipdata['device1_'+istr] != '' and projectipdata['device2_'+istr] != ''):
            connect_schema = {}
            connect_schema['vlan'] = int(projectipdata['vlan_'+istr])
            connect_schema['childsubnet'] = projectipdata['subnet_'+istr]
            connect_schema['device1'] = projectipdata['device1_'+istr]
            connect_schema['device2'] = projectipdata['device2_'+istr]
            connectids.append(insert_into_model(db, connect_schema, models.Connect))
        else:
            connectids.append(None)
    iptable_schema = {}
    proj_id = db.query(models.Project)\
        .filter(models.Project.projectid == projectipdata['projectid'])\
        .filter(models.Project.facility == projectipdata["facility"])\
        .filter(models.Project.vrfname ==  projectipdata["vrfname"])\
        .filter(models.Project.projectname == projectipdata["projectname"])\
        .first()
    
    proj_id = proj_id.__dict__["id"]
    
    iptable_schema['projectid'] = proj_id
    iptable_schema['connection'] = projectipdata['connectivitytype']
    for i in range(4):
        if connectids[i] is not None:
            iptable_schema['connect'+str(i+1)] = connectids[i].id
        else:
            iptable_schema['connect'+str(i+1)] = -1
    return insert_into_model(db, iptable_schema, models.Iptable)

def create_connect(db: Session, connect: schemas.ConnectCreate):
    return insert_into_model(db, connect, models.Connect)

def get_connect(id: int , db:Session):
    return db.query(models.Connect).filter(models.Connect.id==id).first()

def get_all_connect(db):
    return db.query(models.Connect).all()

def get_iptable(id: int , db:Session):
    return db.query(models.Iptable).filter(models.Iptable.id==id).first()

def delete_iptable(id: int, db: Session):
    row = db.query(models.Iptable).filter(models.Iptable.id == id).first()
    status = db.query(models.Iptable).filter(models.Iptable.id == id).delete()
    connect_ids = [
        row.__dict__["connect1"],
        row.__dict__["connect2"],
        row.__dict__["connect3"],
        row.__dict__["connect4"]
    ]
    for c in connect_ids:
        if c != -1:
            db.query(models.Connect).filter(models.Connect.id == c).delete()
    db.commit()
    return status

def get_output_data(id : int, db: Session):
    iptable = db.query(models.Iptable).filter(models.Iptable.id == id).first()
    project = db.query(models.Project).filter(models.Project.id == iptable.__dict__["projectid"]).first()
    facility = project.__dict__["facility"]
    asnumber= db.query(models.Asnumber).filter(models.Asnumber.facility == facility).first()
    try:
        asnumber = asnumber.__dict__["name"]
    except:
        asnumber = ""
    sample_data = []
    connections = []
    for i in range(1,5):
        con = iptable.__dict__["connect"+str(i)]
        if con != -1:
            connections.append(db.query(models.Connect).filter(models.Connect.id == con).first())
        else:
            connections.append(None)


    keys = ["device1", "device2", "vlan"]
    for i in range(4):
        inp = {}
        if connections[i] != None:
            for key in keys:
                try:
                    inp[key] = connections[i].__dict__[key]
                except:
                    inp[key] = ""
                inp["subnet"], inp["entervalue"] = connections[i].__dict__["childsubnet"].split("/")
        else :
            for key in keys:
                inp[key] = ""
        sample_data.append(inp)

    return {
        "data": {
            "projectname": project.__dict__["projectname"],
            "projectid": project.__dict__["projectid"],
            "asnumber": asnumber,
            "vrfname": project.__dict__["vrfname"],
            "connectivitytype": iptable.__dict__["connection"],
            "connect1data": sample_data[0],
            "connect2data": sample_data[1],
            "connect3data": sample_data[2],
            "connect4data": sample_data[3],
        }
    }

def delete_project_id(projectname, projectid, vrfname, facility, db):
    pobj = models.Project
    project = db.query(pobj).filter(pobj.projectid == projectid).filter(pobj.projectname == projectname).filter(pobj.vrfname == vrfname).filter(pobj.facility == facility).first()
    proj_id = project.__dict__["id"]
    ip_entry = db.query(models.Iptable).filter(models.Iptable.projectid == proj_id).first()
    return delete_iptable(ip_entry.__dict__["id"], db=db)

def get_subnet_filtered(facility, entervalue, db):
    parent_subnet = db.query(models.Parentsubnet).filter(models.Parentsubnet.facility==facility).first()
    parent_subnet = parent_subnet.__dict__["parentsubnet"]
    return db.query(models.Subnet).filter(models.Subnet.parentsubnet==parent_subnet).filter(models.Subnet.childsubnet.endswith("/"+str(entervalue))).first()


def delete_all_connections(db):
    status = db.query(models.Connect).delete()
    db.commit()
    return status