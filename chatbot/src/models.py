from sqlalchemy import Column, Integer, String
from src.db import Base

class NumeroEmpresa(Base):
    __tablename__ = "numeroEmpresa"
    empresa = Column(String(255), index=True)  
    numero = Column(String(50),primary_key=True, index=True)