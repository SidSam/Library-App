from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Book

engine = create_engine('sqlite:///libraryapp.db')
# Bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the session won't be persisted into the database until you call session.commit(). 
# If you're not happy about the changes, you can revert all of them back to the last commit by calling session.rollback()
session = DBSession()

#Add a Dummy User
User1 = User(name = 'Lucy Cloudy', email = 'lucycloudy@gmail.com')
session.add(User1)
session.commit()

#Add books
Book1 = Book(name = "Harry Potter and Philosopher's Stone", author = 'J. K. Rowling', picture = "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher's_Stone_Book_Cover.jpg")
session.add(Book1)
session.commit()

Book2 = Book(name = 'Atlas Shrugged', author = 'Ayn Rand', picture = 'https://upload.wikimedia.org/wikipedia/en/8/84/AtlasShrugged.jpg')
session.add(Book2)
session.commit()

Book3 = Book(name = 'Nineteen Eighty-Four', author = 'George Orwell', picture = 'https://upload.wikimedia.org/wikipedia/en/c/c3/1984first.jpg')
session.add(Book3)
session.commit()

Book4 = Book(name = 'Dune', author = 'Frank Herbert', picture = 'https://upload.wikimedia.org/wikipedia/en/5/5a/FrankHerbert_Dune_1st.jpg')
session.add(Book4)
session.commit()

Book5 = Book(name = 'The Godfather', author='Mario Puzo', picture = 'https://upload.wikimedia.org/wikipedia/en/f/f4/Godfather-Novel-Cover.png')
session.add(Book5)
session.commit()

Book6 = Book(name = 'Adventures of Huckleberry Finn', author = 'Mark Twain', picture = 'https://upload.wikimedia.org/wikipedia/commons/6/61/Huckleberry_Finn_book.JPG')
session.add(Book6)
session.commit()

Book7 = Book(name = "The Hitchhiker's Guide to the Galaxy", author = 'Douglas Adams', picture = 'https://upload.wikimedia.org/wikipedia/en/b/bd/H2G2_UK_front_cover.jpg')
session.add(Book7)
session.commit()

Book8 = Book(name = 'Diary of a Wimpy Kid', author = 'Jeff Kinney', picture = 'https://upload.wikimedia.org/wikipedia/en/0/09/Diary_of_a_wimpy_kid.jpg')
session.add(Book8)
session.commit()

Book9 = Book(name = 'Strange Case of Dr Jekyll and Mr Hyde', author = 'R. L. Stevenson', picture = 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Jekyll_and_Hyde_Title.jpg')
session.add(Book9)
session.commit()

Book10 = Book(name = 'Farenheit 451', author = 'Ray Bradbury', picture = 'https://upload.wikimedia.org/wikipedia/en/d/db/Fahrenheit_451_1st_ed_cover.jpg')
session.add(Book10)
session.commit()