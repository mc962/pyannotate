import os
from urllib.parse import urlparse


def parse_db_adapter():
    db_uri = os.environ['DATABASE_URL']
    uri_components = urlparse(db_uri)
    db_type = uri_components.scheme

    if db_type == 'postgres':
        DbAdapter.load_pg_adapter()
    elif db_type == 'sqlite3':
        raise NotImplementedError
    elif db_type == 'mysql':
        raise NotImplementedError


def load_pg_adapter():
    import psycopg2


def load_sqlite3_adapter():
    pass
    # import sqlite3


def load_mysql_adapter():
    pass
    # import MySQLdb
