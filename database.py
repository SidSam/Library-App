from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	name = Column(String(30), nullable = False)
	id = Column(Integer, primary_key = True)
	email = Column(String(250), nullable=False)

class Book(Base):
	__tablename__ = 'book'

	id = Column(Integer, primary_key = True)
	name = Column(String(20), nullable = False)
	author = Column(String(40), nullable = False)
	picture = Column(String(50))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
		'name': self.name,
		'author': self.author,
		'picture': self.picture,
		'id': self.id
		}

engine = create_engine('sqlite:///libraryapp.db')

Base.metadata.create_all(engine)


