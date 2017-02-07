'''
Application error handlers.
'''
from app.models.s3 import S3ClientError
from app.models.threatstack import ThreatStackError
from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(S3ClientError)
@errors.app_errorhandler(ThreatStackError)
def handle_threatstack_error(error):
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': str(error.args)
        }
    }

    return jsonify(response), status_code

@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }

    return jsonify(response), status_code
