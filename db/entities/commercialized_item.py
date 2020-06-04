from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, Column, ForeignKey
from sqlalchemy.orm import relationship


class CommercializedItem(MySql.Base):
    __tablename__ = 'commercialized_items'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    transaction_id = Column(INTEGER, ForeignKey('transactions.id'))
    #transactions = relationship('Transaction', back_populates="commercialized_items")
    item_id = Column(INTEGER, ForeignKey('items.id'))
    #items = relationship('Item', back_populates="commercialized_items")

    def __str__(self):
        return "Category <id=%s transaction_id=%s item_id=%s>" % (self.id, self.transaction_id, self.item_id)