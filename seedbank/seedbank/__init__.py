from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from seedbank.models import (
        DBSession,
        Base,
        )

from seedbank.views import (
        CollectionView,
        )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    # Static route (to static files)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Root-level routes
    config.add_route('home', '/')
    
    # Routes for models.Collection
    config.add_route('collection_index', "/collections/$")
    config.add_route('collection_add', "/collections/add/$")
    config.add_route('collection_view', "/collections/{voucher}/")

    # Make the wsgi app
    config.scan()
    return config.make_wsgi_app()
