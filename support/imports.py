from config import bd_user, bd_password, bd_database

import hashlib
from datetime import datetime

# для работы с Flask
from flask import Flask, jsonify, request
from flask.views import MethodView

# для работы с БД
import sqlalchemy
from sqlalchemy import (create_engine, Column, exc,
                        MetaData, Table, Boolean, DateTime,
                        Index, Text, Integer, String, desc, between,
                        DateTime, BIGINT, TIMESTAMP,
                        PrimaryKeyConstraint,
                        UniqueConstraint,
                        ForeignKeyConstraint,
                        ForeignKey,
                        Numeric)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, relationship
Base = declarative_base() # класс от которого наследуются класс таблиц


class BaseService(object):
    engine = sqlalchemy.create_engine(f'postgresql://{bd_user}:{bd_password}@localhost:5432/{bd_database}')
    session = sessionmaker(bind=engine)
    session = Session(bind=engine)

connection = BaseService.engine.connect()

from models import User, Ad
