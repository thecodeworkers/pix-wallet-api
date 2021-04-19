from flask import request
from ..config.constant import APP_KEY, APP_SECRET
from ..config.keys import verify_application_token

def verify_app_token():
    try:
        headers = request.headers
        if 'X-Api-Key' not in headers:
            raise Exception('Please provide the app token')

        token = headers['X-Api-Key']

        if not verify_application_token(APP_KEY, APP_SECRET, token):
            raise Exception('Token is invalid')

        pass

    except Exception as e:
        pass
        # api_abort(401, e)
