from graphene import ObjectType, List
from ....types import Currency
from . import get_all

class CurrencyQuery(ObjectType):
    currencies = List(Currency)

    def resolve_currencies(root, info):
        return get_all()
