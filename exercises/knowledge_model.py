from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__= "article"
	article_id=Column(Integer,primary_key=True)
	topic=Column(String)
	title=Column(String)
	rating=Column(Integer)

	def __repr__(self):
		return ("if you want to learn about {},""you should look at the wiki articleb called {}"" We gave this article a rating of {} out of 10!").format(
					self.topic,
					self.title,
					self.rating)


