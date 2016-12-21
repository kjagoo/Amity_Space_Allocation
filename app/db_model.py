import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
	"""Create people table
	"""
	__tablename__ = 'person'
	person_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String, nullable=False)
	designation = Column(String, nullable=False)


class Room(Base):
	"""Create the rooms table
	"""
	__tablename__ = 'room'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32), nullable=False)
	rtype = Column(String(32), nullable=False)
	capacity = Column(Integer, nullable=False)


class RoomAllocations(Base):
	"""Store office allocations"""
	__tablename__ = "room_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)
	members = Column(String(250))


class LivingSpaceAllocations(Base):
	"""Store living space allocations"""
	__tablename__ = "livingspace_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)
	members = Column(String(250))

class OfficeAllocations(Base):
	"""Store living space allocations"""
	__tablename__ = "office_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)
	members = Column(String(250))
