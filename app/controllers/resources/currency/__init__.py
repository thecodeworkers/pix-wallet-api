from ....decorators.common import log_record
from ....utils.api import success_operation

@log_record
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

    return success_operation(__name__, get_all.__name__, response)
