#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tabelname__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engien('mysql

