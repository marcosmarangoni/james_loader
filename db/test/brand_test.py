from db.mysql import MySql
from db.entities.brand import Brand
from sqlalchemy.exc import SQLAlchemyError


def create_test():
    session = MySql().get_session()
    try:
        newBrand = Brand(name='TestingOrm', code='123321123')
        session.add(newBrand)
        session.commit()
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()
    pass


def read_test():
    session = MySql().get_session()
    try:
        brands = session.query(Brand).all()
        for brand in brands:
            print(brand)
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()


def update_test():
    session = MySql().get_session()
    try:
        brand = session.query(Brand).first()
        brand.name = 'TestBrandUpdate'
        session.commit()
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()


def delete_test():
    session = MySql().get_session()
    try:
        brand = session.query(Brand).first()
        session.delete(brand)
        session.commit()
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()
    pass


if __name__ == '__main__':
    delete_test()
    read_test()
