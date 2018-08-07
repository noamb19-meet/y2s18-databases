from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,title,rating):
	article_object= Knowledge(
		topic=topic,
		title=title,
		rating=rating)
	session.add(article_object)
	session.commit()

def query_all_articles():
	articles=session.query(Knowledge).all()
	return articles
	

def query_article_by_topic(their_topic):
	article=session.query(Knowledge).filter_by(topic=their_topic).first()
	return article

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()
	

def delete_all_articles():
	session.query(Knowledge).delete()
	
	session.commit()

def edit_article_rating():

	pass

#add_article("dogs","all about dogs",8)
#print(query_all_articles())

#print(query_article_by_topic("cats"))
#delete_article_by_topic("dogs")
delete_all_articles()
