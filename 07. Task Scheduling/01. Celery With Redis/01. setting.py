# Install Celery
pip install celery

# Install Redis (if not installed)
# Windows, Download : https://www.memurai.com/
# Macos, Download   : https://redis.io/docs/install/install-redis/install-redis-on-mac-os/
# For Ubuntu
sudo apt update
sudo apt install redis-server

# For other systems, refer to the Redis installation guide


# Celery configuration for Redis as the broker
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'      # or 'redis://localhost:6379/0'    -> in live server   'redis://domain_or_ip:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # or 'redis://localhost:6379/0'    -> in live server   'redis://domain_or_ip:6379/0'  
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
