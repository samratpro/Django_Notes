# my_logger.py   in App Folder

import logging
import sys

class PrintLogger:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)

    def write(self, message):
        self.logger.info(message)

# Initialize the custom logger with a specific name related to the module or purpose
sys.stdout = PrintLogger('my_app.debug_logs')  # Replace with a descriptive name
