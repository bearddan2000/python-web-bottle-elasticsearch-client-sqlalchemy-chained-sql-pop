import os
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DbModel(Base):
    __tablename__ = os.environ["INDEX_NAME"]
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    color = Column(String(10))

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "<Pop('%d', %s', '%s')>" % (self.id, self.name, self.color)
