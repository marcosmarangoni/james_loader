from sqlalchemy.orm import relationship

from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, Column


class Category(MySql.Base):
    __tablename__ = 'categories'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    products = relationship('Product', back_populates="categories")
    name = Column(VARCHAR(50))

    def __str__(self):
        return "Category <id=%s name=%s>" % (self.id, self.name)
