def format_response(status_code, status_message, response):
    return {
        'status': status_code,
        'message': status_message,
        'response': response
    }
