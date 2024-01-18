import logging
import sys
from django.conf import settings
from pathlib import Path


# path 
# logs / console.log  

# Configure the root logger to capture all messages
logging.basicConfig(level=logging.DEBUG)

# Add a StreamHandler to capture messages to the console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)

# Add a FileHandler to capture messages to a log file
file_handler = logging.FileHandler(Path(settings.BASE_DIR) / 'logs' / 'console.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

# Now, when you use the print function, the messages will be captured by the logging handlers
print('This message will be captured by the logging handlers')
