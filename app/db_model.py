import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class PersonDb(Base):
	"""Create people table
	"""
	__tablename__ = 'person'
	person_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(32), nullable=False)
	role = Column(String(32), nullable=False)

class UnallocatedPerson(Base):
	"""Create unallocated_persons table
	"""
	__tablename__ = 'unallocated_persons'
	person_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(32), nullable=False)
	

class AllocatedPerson(Base):
	"""Create allocated people table
	"""
	__tablename__ = 'allocated_persons'
	person_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(32), nullable=False)



class AvailableRooms(Base):
	"""Create the available_rooms table
	"""
	__tablename__ = 'available_rooms'
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)

class RoomAllocations(Base):
	"""Store room allocations"""
	__tablename__ = "room_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)
	members = Column(String(250))


class LivingSpaceAllocations(Base):
	"""Store living space rooms"""
	__tablename__ = "livingspace_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)
	rm_type = Column(String(250))

class OfficeAllocations(Base):
	"""Store office rooms"""
	__tablename__ = "office_allocations"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(32), nullable=False)
	rm_type = Column(String(250))

class DatabaseCreator(object):
	"""Creates a db connection object"""

	def __init__(self, db_name="default_db"):
		self.db_name = db_name
		if self.db_name:
			self.db_name = db_name + '.sqlite'
		else:
			self.db_name = 'main.sqlite'
		self.engine = create_engine('sqlite:///' + self.db_name)
		self.session = sessionmaker()
		self.session.configure(bind=self.engine)
		Base.metadata.create_all(self.engine)
