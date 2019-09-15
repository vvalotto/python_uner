
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


engine_sqlite = create_engine('sqlite:///prueba.db', echo=True)

Base = declarative_base()
Base.metadata.bind = engine_sqlite
Base.metadata.create_all()
