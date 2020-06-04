from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


class MySql:
    Base = declarative_base()

    def __init__(self):
        self.engine = create_engine('mysql://marcos:h1market@2018@35.239.190.88:3306/james')
        #self.Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return sessionmaker(bind=self.engine)()
