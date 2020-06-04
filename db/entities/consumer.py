from sqlalchemy.orm import relationship

from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, Column


class Consumer(MySql.Base):
    __tablename__ = 'consumers'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    #transactions = relationship('Transaction', back_populates="consumers")
    name = Column(VARCHAR(50))
    personal_code = Column(VARCHAR(50))

    def __str__(self):
        return "Category <id=%s name=%s personal_code=%s>" % (self.id, self.name, self.personal_code)
