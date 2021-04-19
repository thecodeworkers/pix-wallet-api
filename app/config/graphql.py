from flask_graphql import GraphQLView
from graphene import Schema
from ..middlewares import verify_app_token
from ..controllers import *

class AllQuerys(
    CurrencyQuery
):
    pass

class AllMutations(

):
    pass


schema = Schema(
    query=AllQuerys
    # mutation=AllMutations
)

def init_graphql(app):
    app.add_url_rule('/graphql/', view_func=GraphQLView.as_view(
        'Pix Wallet',
        schema=schema,
        graphiql=True,
        middleware=[verify_app_token]
    ))
