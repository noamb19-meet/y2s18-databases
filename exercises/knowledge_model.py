from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="person"
	person_id=Column(Integer,primary_key=True)e
	name=Column(String)
	fav_color=Column(String)
	fav_animal=Column(String)

	def__repr__(self):
		return ("name:{}\n"
				"favorite_color:{}\n"
				"favorite_animal:{}\n").format(
					self.name,
					self.fav_color,
					self.fav_animal)


