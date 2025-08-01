# INSTALLED_APPS list tells django to include our app in the project files
import os
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'myApp'
]

TEMPLATES=[
    {
        'DIRS': [os.path.join(BASE_DIR, 'myApp/templates')],
    }
]