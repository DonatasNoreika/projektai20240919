from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Projektas(Base):
    __tablename__ = "Projektas"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    price = Column("Kaina", Float)
    created_date = Column("Sukūrimo data", DateTime, default=datetime.today)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

# Create the engine here
engine = create_engine('sqlite:///projektai.db')
Base.metadata.create_all(engine)