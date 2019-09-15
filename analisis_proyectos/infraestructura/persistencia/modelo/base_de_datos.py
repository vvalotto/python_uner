"""
Definición del modelo de datos y declaración de las tablas del modelo
"""
from uuid import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class UnidadAcademicaDTO(Base):
    """
    Tabla Unidad Academica
    """
    __tablename__ = "td_unidad_academica"

    id = Column(String(36), primary_key=True)
    nombre_unidad_academica = Column(String(200), nullable=False)
    nombre_universidad = Column(String(200), nullable=False)
    domicilio_calle = Column(String(50), nullable=False)
    domicilio_numero = Column(String(50), nullable=False)
    domicilio_piso = Column(String(20), nullable=False)
    domicilio_depto = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Unidad Academica (nombre='%s', universidad='%s'>"\
            % (self.nombre_unidad_academica, self.nombre_universidad)


class CarreraDTO(Base):
    """
    Tabla Carrera, relacionada con Unidad Academica
    """
    __tablename__ = "td_carrera"

    id = Column(String(36), primary_key=True)
    nombre_carrera = Column(String(100), nullable=False)
    codigo_carrera = Column(String(20), nullable=False)
    id_unidad_academica = Column(String(36), ForeignKey(UnidadAcademicaDTO.id))


class MateriaDTO(Base):
    """
    Tabla Materia, relacionada con Carrera
    """
    __tablename__ = "td_materia"

    id = Column(String(36), primary_key=True)
    codigo_materia = Column(String(20), nullable=False)
    nombre_materia = Column(String(100), nullable=False)
    plan = Column(String(20), nullable=False)
    id_materia = Column(String(36), ForeignKey(CarreraDTO.id))
