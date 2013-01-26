from pyramid.response import Response
from pyramid.view import (
        view_config,
        view_defaults,
        )

from sqlalchemy.exc import DBAPIError

from .models import (
        DBSession,
        Collection,
        User,
        Species,
        Trip,
        )


@view_config(route_name='home', renderer='home.mak')
def my_view(request):
    try:
        one = None
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'seedbank'}


class CollectionView(object):
    __autoexpose__ = None
    def __init__(self, request):
        self.request = request
    
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
