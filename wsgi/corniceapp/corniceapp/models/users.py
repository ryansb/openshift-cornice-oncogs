import cryptacular.bcrypt

from sqlalchemy import Column

from sqlalchemy.orm import synonym

from sqlalchemy.types import (
    Integer,
    Unicode,
)

from pyramid.security import (
    Everyone,
    Authenticated,
    Allow,
)

from corniceapp.models import Base, DBSession

crypt = cryptacular.bcrypt.BCRYPTPasswordManager()


def hash_password(password):
    return unicode(crypt.encode(password))


class User(Base):
    """
    Application's user model.
    """
    __tablename__ = 'users'
    id_ = Column(Integer, primary_key=True)
    username = Column(Unicode(32), unique=True)
    name = Column(Unicode(64))
    email = Column(Unicode(64))

    _password = Column('password', Unicode(64))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, username=None, password=None, name=None, email=None):
        if username: self.username = username
        if name: self.name = name
        if email: self.email = email
        if password: self.password = password

    def to_dict(self):
        return dict(
            username=self.username,
            name=self.name,
            email=self.email,
            id=self.id_,
        )

    @classmethod
    def get_by_username(cls, username):
        return DBSession.query(cls).filter(cls.username == username).first()

    @classmethod
    def all(cls):
        return DBSession.query(cls).all()

    @classmethod
    def check_password(cls, username, password):
        user = cls.get_by_username(username)
        if not user:
            return False
        return crypt.check(user.password, password)

    def put(self):
        DBSession.add(self)
        DBSession.flush()
