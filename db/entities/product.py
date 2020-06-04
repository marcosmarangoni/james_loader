from db.mysql import MySql
from sqlalchemy import VARCHAR, INTEGER, FLOAT, Column, ForeignKey
from sqlalchemy.orm import relationship


class Product(MySql.Base):
    __tablename__ = 'products'
    ean = Column(VARCHAR(13), primary_key=True)
    brand_id = Column(INTEGER, ForeignKey('brands.id'))
    brands = relationship('Brand', back_populates="products")
    category_id = Column(INTEGER, ForeignKey('categories.id'))
    categories = relationship('Category', back_populates="products")
    name = Column(VARCHAR(500))
    slug = Column(VARCHAR(256))

    def __str__(self):
        return "Item <ean=%s brand_id=%s category_id=%s name=%s slug=%s>" % (
            self.ean, self.brand_id, self.category_id, self.name, self.slug
        )
