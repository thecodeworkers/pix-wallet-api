from graphene import ObjectType, List
from ....types import Currency

class CurrencyQuery(ObjectType):
    currencies = List(Currency)

    def resolve_currencies(root, info):
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
            }
        ]

        return response
        # try:
        #     # auth_token = info.context.headers.get('Authorization')

        # except grpc.RpcError as e:
        #     error_log(info.context.remote_addr, e.details(), 'resources_microservice', type(e).__name__)
        #     raise Exception(message_error(e))
        # except Exception as e:
        #     error_log(info.context.remote_addr, e.args[0], 'resources_microservice', type(e).__name__)
        #     raise Exception(e.args[0])
