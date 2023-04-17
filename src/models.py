import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    description = Column(String(250))
    photourl = Column(String(250))
    usertype = Column(Integer, nullable=False)


class Post(Base):
    __tablename__ = 'post'
    id= Column(Integer, primary_key=True)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    postype = Column(Integer, nullable=False)
    utl = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    to_user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class CommentLike(Base):
    __tablename__ = 'comment_like'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)

class Publicity(Base):
    __tablename__ = 'publicity'
    id = Column(Integer, primary_key=True)
    publicity_level=Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram4.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
