# middleware.py in Related App Folder

import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)  # Change __name__ to your logger name

    def __call__(self, request):
        # Log the request method and path
        self.logger.info(f"Request method: {request.method}, Path: {request.path}")

        response = self.get_response(request)
        return response
