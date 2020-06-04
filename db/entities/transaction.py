from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, Column, ForeignKey, TIMESTAMP, FLOAT
from sqlalchemy.orm import relationship


class Transaction(MySql.Base):
    __tablename__ = 'transactions'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    #commercialized_item = relationship('CommercializedItem', back_populates="transactions")
    store_id = Column(INTEGER, ForeignKey('stores.id'))
    #stores = relationship('Store', back_populates="transactions")
    consumer_id = Column(INTEGER, ForeignKey('consumers.id'))
    #consumers = relationship('Consumer', back_populates="transactions")
    issue_date = Column(TIMESTAMP)
    commercialized_items = Column(INTEGER)
    purchase_total = Column(FLOAT)
    discount = Column(FLOAT)
    doct_number = Column(FLOAT)
    payment_method = Column(VARCHAR(50))

    def __str__(self):
        return "Item <id=%s store_id=%s consumer_id=%s issue_date=%s commercialized_items=%s" \
               " purchase_total=%s discount=%s doct_number=%s payment_method=%s>" % (
                   self.id, self.store_id, self.consumer_id, self.issue_date, self.commercialized_items,
                   self.purchase_total, self.discount, self.doct_number, self.payment_method
               )

