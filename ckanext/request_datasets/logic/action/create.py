# coding: utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

import sqlalchemy

import ckan.plugins.toolkit as toolkit
import ckan.lib.dictization.model_dictize as model_dictize
from ckan.logic import NotAuthorized

import logging
log = logging.getLogger(__name__)

from sqlalchemy import Column, String, DateTime, Sequence, Integer, types, desc
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from ckan.model.domain_object import DomainObject
from ckan.model.meta import metadata, mapper, Session
from ckan import model

import logging
log = logging.getLogger(__name__)

import json
import uuid

base = declarative_base()

def _get_datetime():
    return datetime.now()

def make_uuid():
    return unicode(uuid.uuid4())

class Request(base):
    __tablename__ = 'requests'

    id = Column(types.UnicodeText, primary_key=True, default=make_uuid)
    title = Column(types.UnicodeText, nullable=False, unique=True)
    content = Column(types.UnicodeText, nullable=False)
    email = Column(types.UnicodeText, nullable=False)
    created_date = Column(DateTime, default = _get_datetime)
    update_date = Column(DateTime, onupdate = _get_datetime)
    type = Column(types.UnicodeText, nullable=False, default ='1')

def request_datasets_create(context, data_dict):
    model = context['model']
    model.Session.add(Request(title= data_dict['title'], email=data_dict['email'], content= data_dict['content']))
    model.Session.commit()
    return True
