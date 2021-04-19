from graphene import ObjectType, List
from ....types import Currency

class CurrencyQuery(ObjectType):
    currencies = List(Currency)

    def resolve_currencies(root, info):
        return get_all()

def get_all():
    response = [
        {
            'id': 'sjsjjjalkdhdhd',
            'name': 'Bitcoin',
            'color': 'orange',
            'gradients': [],
            'active': True,
            'type': 'CRYPTO',
            'symbol': 'BTC',
            'price': 52.000
        },
        {
            'id': 'sjsjjjalkdhdhd',
            'name': 'Bitcoin',
            'color': 'orange',
            'gradients': [],
            'active': True,
            'type': 'CRYPTO',
            'symbol': 'BTC',
            'price': 52.000
        }
    ]

    return response
