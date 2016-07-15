import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Unicode, Integer

PATH = sys.path[0]
Base = declarative_base()
engine = create_engine('sqlite:///{}/user.db'.format(PATH), echo=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode, nullable=False, index=True, unique=True)
    firstname = Column(Unicode, nullable=False)
    lastname = Column(Unicode, nullable=False)

    @staticmethod
     def check_input(string):
         '''
         Based on the man page available on
         freebsd.org/cgi/man.cgi?adduser(8)
         '''
         username = re.compile(r'[a-z0-9\-]+')
         firstname = re.compile(r'[a-zA-Z]+')
         lastname = re.compile(r'[a-zA-Z\'\-]+')

    def user():

