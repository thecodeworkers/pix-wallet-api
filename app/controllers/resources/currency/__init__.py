from ....decorators.common import log_record
from ....collections.currencies import Currencies
from ....utils import success_operation, parser_all_object

@log_record
def get_all():
    currencies = Currencies.objects
    currencies = parser_all_object(currencies)

    return success_operation(__name__, get_all.__name__, currencies)
