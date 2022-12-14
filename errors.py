from support.imports import *

from app import app


class BasicException(Exception):
    status_code = 0
    default_message = 'Unknown Error'

    def __init__(self, message: str = None, status_code: int = None):
        super().__init__(message)
        self.message = message
        request.status = self.status_code
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            'message': self.message or self.default_message
        }


class NotFound(BasicException):
    status_code = 404
    default_message = 'NOT_FOUND'


class AuthError(BasicException):
    status_code = 401
    default_message = 'UNAUTHORIZED'


class BadRequest(BasicException):
    status_code = 400
    default_message = 'BAD_REQUEST'


@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
