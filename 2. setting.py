# Setting ------------------------------------------

# App connection..     # Probbaly 33 line
INSTALLED_APPS = [
    'NewApp',
]



# Template Connection..
DIRS': [BASE_DIR / 'templates'], # Probbaly 59 line


# Static File Connection..   # Probbaly 123 line
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# This is for Hosted server and When Debug is False after Hosting Django App in Domain
STATIC_ROOT = BASE_DIR / "staticfiles"
python manage.py collectstatic
# >>> Now configure it in Project urls.py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = []
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# >>> If Debug is True then admin CSS won't work in the local Server
# >>> 404.html and Debug is false for 404 page

# Postgresql database  # Probbaly 78 line
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'samrat',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
    }
}
