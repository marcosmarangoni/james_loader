from sqlalchemy.orm import relationship

from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, Column


class Store(MySql.Base):
    __tablename__ = 'stores'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    #transactions = relationship('Transaction', back_populates="stores")
    name = Column(VARCHAR(50))
    address = Column(VARCHAR(256))
    city = Column(VARCHAR(50))
    state = Column(VARCHAR(500))
    latitude = Column(VARCHAR(20))
    longitude = Column(VARCHAR(50))

    def __str__(self):
        return "Item <id=%s name=%s address=%s city=%s state=%s latitude=%s longitude=%s>" % (
            self.id, self.name, self.address, self.city, self.state, self.latitude, self.longitude
        )
