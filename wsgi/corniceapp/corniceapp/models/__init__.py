from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()


from panstora import db_url
_engine = create_engine(db_url)

DBSession = scoped_session(
    sessionmaker(bind=_engine, extension=ZopeTransactionExtension())
)

from corniceapp.models.users import User
# Import your models here
