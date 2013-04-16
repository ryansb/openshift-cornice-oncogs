from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()


from corniceapp import db_url
_engine = create_engine(db_url)

DBSession = scoped_session(
    sessionmaker(bind=_engine, extension=ZopeTransactionExtension())
)


from corniceapp.models.users import User

# If the database isn't initialized, initialize it!
try:
    User.all()
except ProgrammingError, e:
    import transaction

    metadata = Base.metadata
    metadata.create_all(_engine)

    u = User('ryansb', 'somepass', 'Ryan Brown', 'ryansb@csh.rit.edu')
    u.put()
