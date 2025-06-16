
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'your-very-secure-secret-key-at-least-50-characters-long'
 
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
# )%b$q1!5jeyugb$t-=7(v##s_)6axbg7r8wdex%s_@9j2@rf51

# حالا می‌توانید از متغیرهای محیطی استفاده کنید
# SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    'django.contrib.sites',  # حتما اضافه شود (برای allauth)
    
    # پکیج‌های ثالث
    'rest_framework',
    'rest_framework.authtoken',
    
    'corsheaders',
    'drf_yasg',
    
    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    
    
    
    
    # اپ‌های محلی شما
    'posts',  # یا 'posts.apps.PostsConfig' اگر از AppConfig استفاده می‌کنید
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


from pathlib import Path



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #     'USER': os.getenv('DB_USER'),
    #     'PASSWORD': os.getenv('DB_PASSWORD'),
    #     'HOST': os.getenv('localhost'),
    #     'PORT': os.getenv('5432'),
    # }
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# new

# AUTH_USER_MODEL = 'config.CustomUser '  # اگر از مدل کاربر سفارشی استفاده می‌کنید


SITE_ID = 1


# CORS_ALLOW_ALL_ORIGINS = True
# یا اگر مبدأهای خاصی مد نظر دارید:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost:3000",
]


CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    
    'DEFAULT_THROTTLE_RATES': {
        'anon': '30/day',
        'user': '100/day'
    },
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20 ,
    
    'DEFAULT_SCHEMA_CLASS': 'drf_yasg.openapi.AutoSchema',
}



REST_AUTH = {
    'USE_JWT': True,  # اگر از JWT استفاده می‌کنید
    'JWT_AUTH_COOKIE': 'jwt-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'jwt-refresh-token',
    
    'SESSION_LOGIN': False,
    'OLD_PASSWORD_FIELD_ENABLED': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'REGISTER_SERIALIZER': 'config.serializers.CustomRegisterSerializer',  # اگر نیاز دارید
}


ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'  # سفارشی‌سازی اگر نیاز است
SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'



# Static & Media Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # برای تولید


# تنظیمات دیتابیس
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': os.environ.get('DB_NAME', 'blogdb'), # مقدار پیش‌فرض اضافه شد
        'USER': os.environ.get('DB_USER', 'bloguser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'complexpass123'),
        
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
       
        'OPTIONS': {
            'connect_timeout': 5,  # زمان انتظار برای اتصال
        }

    }
}

# Cache Settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}



# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'WARNING',
    },
}



# Additional Important Settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# اگر از JWT استفاده می‌کنید
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# تنظیمات Swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
}


# در محیط تولید این موارد را فعال کنید
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']  # دامنه واقعی خود را وارد کنید
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')  # از متغیر محیطی بخوانید



# Security Settings (for production)
if not DEBUG:
    SECURE_SSL_REDIRECT = False  # در تولید True شود
    SESSION_COOKIE_SECURE = False  # در تولید True شود
    CSRF_COOKIE_SECURE = False  # در تولید True شود
    SECURE_HSTS_SECONDS = 31536000  # در تولید فعال شود
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# تنظیمات ایمیل
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # در تولید
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# تنظیمات Allauth
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # یا 'optional'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USERNAME_REQUIRED = True




