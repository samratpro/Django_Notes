# Using logger instead of print function, cause live server can't show data like VS Code or Pycharm terminal

import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


def your_view_function(request):
    if condition:
        logger.error('An error occurred')  # Example of logging an error
        # Your error handling code
    else:
        logger.info('This is bulk info posting page, testing for Python logger')
        return render(request, template, context=context)
