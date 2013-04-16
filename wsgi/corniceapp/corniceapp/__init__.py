"""Main entry point
"""
from pyramid.config import Configurator

import os


db_name = "oncogs"

db_url = os.environ["OPENSHIFT_MYSQL_DB_URL"] + db_name


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("corniceapp.views")
    if settings.get('database.url', None):
        db_url = settings.get('database.url')
    return config.make_wsgi_app()
