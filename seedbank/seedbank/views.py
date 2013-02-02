from pyramid.response import Response
from pyramid.view import (
        view_config,
        view_defaults,
        )

from sqlalchemy.exc import DBAPIError

from seedbank.models import (
        DBSession,
        Collection,
        User,
        Species,
        Trip,
        )


class BaseView(object):
    __autoexpose__ = None
    def __init__(self, request):
        self.request = request


class Root(BaseView):
    """Views in the root path
    """
    
    @view_config(route_name='home', renderer='home.mak')
    def home(request):
        return {}


class CollectionView(object):
    """Views for the Collections model
    """

    @view_config(route_name="collection_add", renderer="collection/add.mak")
    def add(self):
        return

    @view_config(route_name="collection_index",
            renderer="collection/index.mak")
    def index(self):
        return {"collections": [
                    {"voucher": "kdm123/13"},
                    {"voucher": "kdm124/13"},
                    ]
                }

    @view_config(route_name="collection_view", renderer="collection/view.mak")
    def view(self):
        return {"voucher": "kdm123/13"}
