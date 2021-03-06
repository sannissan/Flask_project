import sqlalchemy as sa

from sqlalchemy.orm import mapper
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker



ROLE_USER = 0
ROLE_ADMIN = 1

print("Версия SQLAlchemy:", sa.__version__)
engine = sa.create_engine('sqlite:///maxipro.db', echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    print("Создана база данных")
    create_database(engine.url)


def print_table(_session, _table):
    print()
    print(_table, "-----------------------------------")
    for instance in _session.query(_table).all():
        print(instance)
    print("------------------------------------------")


class User(object):
    def __init__(self, user_id, nickname, email, role):
        self.user_id = user_id
        self.nickname = nickname
        self.email = email
        self.role = role

    def __repr__(self):
        return '<User %s %s>' % (self.nickname, self.role)


class Catalog(object):
    def __init__(self, code, name, id_category):
        self.code = code
        self.name = name
        self.id_category = id_category

    def __repr__(self):
        return "<Catalog('%s','%s', '%s')>" % (self.code, self.name, self.id_category)


class Category(object):
    def __init__(self, category, level):
        self.category = category
        self.level = level

    def __repr__(self):
        return "<Category('%s','%s', '%s')>" % (self.id_category, self.category, self.level)


metadata = MetaData()
catalog_table = Table('catalog',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('code', String),
                      Column('name', String),
                      Column('id_category', String))

category_table = Table('сategories',
                       metadata,
                       Column('id', Integer, primary_key=True),
                       Column('category', String),
                       Column('level', String))

metadata.create_all(engine)
mapper(Catalog, catalog_table)
mapper(Category, category_table)



