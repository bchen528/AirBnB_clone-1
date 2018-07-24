#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
#from models.state import State
from sqlalchemy import Column, String, ForeignKey
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""
