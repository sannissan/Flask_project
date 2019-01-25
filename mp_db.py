import sqlalchemy as sa
import requests
import json

from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy_utils import database_exists, create_database

print("Версия SQLAlchemy:", sa.__version__)
engine = sa.create_engine('sqlite:///maxipro.db', echo=False)

if not database_exists(engine.url):
    print("Создана база данных")
    create_database(engine.url)


def print_table(_session, _table):
    print()
    print(_table,"-----------------------------------")
    for instance in _session.query(_table).all():
        print(instance)
    print("------------------------------------------")


class Catalog(object):
    def __init__(self, code, name, id_category):
        self.code = code
        self.name = name
        self.id_category = id_category

    def __repr__(self):
        return "<Catalog('%s','%s', '%s')>" % (self.code, self.name, self.id_category)


class Category(object):
    def __init__(self, id_category, category, level):
        self.id_category = id_category
        self.category = category
        self.level = level
        self.category = category

    def __repr__(self):
        return "<Category('%s','%s', '%s')>" % (self.id_category, self.category, self.level)


metadata = MetaData()
catalog_table = Table('catalog', metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String),
    Column('name', String),
    Column('id_category', String)
)
category_table = Table('Category', metadata,
    Column('id_category', Integer, primary_key=True),
    Column('code', String),
    Column('name', String)
)
metadata.create_all(engine)
mapper(Catalog, catalog_table)



