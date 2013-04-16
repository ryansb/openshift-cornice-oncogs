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
    return {"users": [u.to_dict() for u in User.all()]}

#@users.post()
#def post_users(request):
#    request
#    return
