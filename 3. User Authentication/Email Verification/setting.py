
EMAIL_HOST_PASSWORD = 'dzkaxrblycvbdtfg'   
# Step 1: https://myaccount.google.com/
# Step 2: From Security section turn on 2 step verification
# Step 3: Search with " App Passwords "
# Step 4 : Create App selete others and generate token


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mdsamrat25800@gmail.com'
EMAIL_HOST_PASSWORD = 'dzkaxrblycvbdtfg'   
DEFAULT_FROM_EMAIL = 'mdsamrat25800@gmail.com'
PASSWORD_RESET_TIMEOUT = 14400  # Seconds


# user_profile_project/settings.py
AUTH_USER_MODEL = 'user_profile.UserProfile'   # ` user_profile ` is app name and ` UserProfile ` is classname that have in models.py

