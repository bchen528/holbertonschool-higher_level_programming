#!/usr/bin/python3
"""creates State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
from sys import argv


db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3])
Base = declarative_base()


class State(Base):
    """class State"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
