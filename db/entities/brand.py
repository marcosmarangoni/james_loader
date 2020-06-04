from sqlalchemy.orm import relationship

from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, Column


class Brand(MySql.Base):
    __tablename__ = 'brands'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    products = relationship('Product', back_populates="brands")
    name = Column(VARCHAR(100))
    code = Column(VARCHAR(50))

    def __str__(self):
        return "Brand <id=%s name=%s  code=%s>" % (self.id, self.name, self.code)
