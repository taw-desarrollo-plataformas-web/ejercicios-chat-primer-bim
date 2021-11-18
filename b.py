from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///demobase3.db') 

Base = declarative_base()

class Hospital():
    __tablename__ = 'hospital'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    numero_camas = Column(Integer)
    numero_pisos = Column(Integer)
    ciudad = Column(String)
    provincia = Column(String)
    
    def __repr__(self):
        return "Hospital: %s - camas: %d - pisos: %d \n%s %s" % (
                          self.nombre, 
                          self.numero_camas, 
                          self.numero_pisos,
                          self.ciudad,
                          self.provincia)

Base.metadata.create_all(engine)
