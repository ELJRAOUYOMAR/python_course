# SQLAlchemy 

## Introduction
SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It allows you to interact with databases using Python objects instead of writing raw SQL queries. Here's a comprehensive tutorial to get you started with SQLAlchemy:

## 1. Installation
First, you need to install SQLAlchemy. You can do this using pip:
```Bash
First, you need to install SQLAlchemy. You can do this using pip:
```

## 2. Creating an Engine
The engine is the starting point for any SQLAlchemy application. It represents the core interface to the database.
```python
from sqlalchemy import create_engine

# Replace 'sqlite:///example.db' with your database URL
engine = create_engine('sqlite:///example.db', echo=True)
```

## 3. Defining Models
Models are Python classes that represent database tables. You define models by subclassing Base, which is created using the declarative_base function.

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"
```

## 4. Creating Tables
To create the tables defined by your models, use the create_all method of the engine.

```python
Base.metadata.create_all(engine)
```

## 5. Working with Sessions
A session is used to interact with the database. You create a session using a sessionmaker.

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

## 6. Adding and Querying Data
You can add new records to the database by creating instances of your models and adding them to the session.

```python
# Add a new user
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Query the user
user = session.query(User).filter_by(name='John Doe').first()
print(user)
```

## 7. Updating and Deleting Data
Updating and deleting records is straightforward. You can modify attributes of an instance and commit the session to update the database.

```python
# Update user
user.age = 31
session.commit()

# Delete user
session.delete(user)
session.commit()
```

## 8. Using Relationships
SQLAlchemy allows you to define relationships between models. Here's an example with a Post model related to the User model.
```python
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='posts')

User.posts = relationship('Post', order_by=Post.id, back_populates='user')
```

## 9. Creating and Querying Related Data
```python
# Add a post for the user
new_post = Post(title='My First Post', content='Hello World!', user=user)
session.add(new_post)
session.commit()

# Query posts
user_with_posts = session.query(User).filter_by(name='John Doe').first()
for post in user_with_posts.posts:
    print(post.title, post.content)
```

## 10. Advanced Queries
SQLAlchemy provides a powerful query API for complex queries.

```python
# Filter users by age
young_users = session.query(User).filter(User.age < 30).all()

# Join users and posts
user_posts = session.query(User, Post).filter(User.id == Post.user_id).all()
for u, p in user_posts:
    print(u.name, p.title)
```

## 11. Handling Migrations
For database schema changes, you can use Alembic, a lightweight database migration tool for SQLAlchemy.

First, install Alembic:

```python
pip install alembic
```

Then, set up Alembic in your project:
```python
alembic init alembic
```

Configure alembic.ini and env.py as needed, then use Alembic commands to manage migrations:
```python
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Summary

SQLAlchemy is a robust and flexible ORM that allows you to interact with databases using Python objects. This tutorial covers the basics of setting up SQLAlchemy, defining models, creating tables, working with sessions, and performing CRUD operations. With SQLAlchemy, you can also define relationships between models and perform complex queries.


## Same Links:
- https://docs.sqlalchemy.org/en/13/orm/tutorial.html
- https://www.fullstackpython.com/object-relational-mappers-orms.html
- https://docs.sqlalchemy.org/en/13/
- https://www.youtube.com/watch?v=woKYyhLCcnU
- https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW
- https://www.pythonsheets.com/notes/python-sqlalchemy.html

