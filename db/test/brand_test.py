from db.mysql import MySql
from db.entities.brand import Brand
from sqlalchemy.exc import SQLAlchemyError


def create_test():
    session = MySql().get_session()
    try:
        brands = session.query(Brand).whereclause(Brand.id == 1)
        for brand in brands:
            print(brand)
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()
    pass


def read_test():
    session = MySql().get_session()
    try:
        brands = session.query(Brand).filter_by(id=1)
        for brand in brands:
            print(brand)
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()


def update_test():
    session = MySql().get_session()
    try:
        brands = session.query(Brand).whereclause(Brand.id == 1)
        for brand in brands:
            print(brand)
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()


def delete_test():
    session = MySql().get_session()
    try:
        brands = session.query(Brand).whereclause(Brand.id == 1)
        for brand in brands:
            print(brand)
    except SQLAlchemyError as error:
        print(error)
    finally:
        session.close()
    pass


if __name__ == '__main__':
    read_test()
