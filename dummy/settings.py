import os
import environ
import dj_database_url
from datetime import timedelta
from pathlib import Path

# Initialize environ and read the .env file
env = environ.Env()
environ.Env.read_env() # Reads the .env file located at the same directory level

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

# ALLOWED_HOSTS must include localhost, 127.0.0.1, and the Render domain pattern
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'cloudinary', # <--- Added for Cloudinary integration
    
    # Your apps
    'accounts',
    'products',
    'comments',
]

# Custom User Model
AUTH_USER_MODEL = 'accounts.User' 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <--- Added for production static file serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Note: CsrfViewMiddleware remains here, but DRF's authentication
    # settings below will bypass it for token-authenticated requests.
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dummy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dummy.wsgi.application'


# Database (Supabase/PostgreSQL Configuration)

# This uses dj_database_url to parse the Supabase connection string from .env
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) for WhiteNoise
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
# This is the directory WhiteNoise will look into for collected static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# ----------------------------------------------------------------------
# DRF, JWT, and MEDIA Configuration (CRITICAL FOR AUTH AND IMAGE UPLOADS)
# ----------------------------------------------------------------------

# 1. Django REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 1. Use JWT Bearer token authentication by default (Priority 1)
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 2. Keep SessionAuthentication for DRF's browsable API
        'rest_framework.authentication.SessionAuthentication', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # Set default to require login for all endpoints
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# 2. JWT Configuration (Controls token lifespan and format)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',), # Tells Django to look for 'Bearer [token]'
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# 3. Cloudinary Media File Settings (Replaces local media storage)

# Load Cloudinary credentials from .env
CLOUDINARY_CLOUD_NAME = env('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = env('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = env('CLOUDINARY_API_SECRET')

# Configure Django to use Cloudinary for all file uploads (prodImg)
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'