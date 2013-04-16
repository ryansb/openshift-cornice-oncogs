""" Cornice services.
"""
from cornice import Service
from corniceapp.models.users import User


hello = Service(name='hello', path='/', description="Simplest app")
users = Service(name='users', path='/users', description="For learning about users.")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

@users.get()
def get_users(request):
    return User.all()
