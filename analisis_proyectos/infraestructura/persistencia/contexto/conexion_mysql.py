import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


pymysql.install_as_MySQLdb()

engine_mysql = create_engine('mysql+pymysql://pysea_admin:pysea@localhost:3306/pysea')

Base = declarative_base()


class UnidadAcademicaDTO(Base):
    __tablename__ = "td_unidad_academica"

    id = Column(String(36), primary_key=True)
    nombre_unidad_academica = Column(String(200))
    nombre_universidad = Column(String(200))
    domicilio_calle = Column(String(50))
    domicilio_numero = Column(String(50))
    domicilio_piso = Column(String(20))
    domicilio_depto = Column(String(50))


Base.metadata.bind = engine_mysql
Base.metadata.create_all()
