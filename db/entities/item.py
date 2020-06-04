from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, FLOAT, Column
from sqlalchemy.orm import relationship


class Item(MySql.Base):
    __tablename__ = 'items'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    #commercialized_items = relationship('CommercializedItem', back_populates="items")
    ean = Column(VARCHAR(13))
    price = Column(FLOAT)

    def __str__(self):
        return "Item <id=%s ean=%s price=%s>" % (self.id, self.ean, self.price)
