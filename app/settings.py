import os
from pathlib import Path

from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define o modo de execução da aplicação
MODE = os.getenv("MODE")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False")
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://localhost:8000", "https://*.fl0.io/"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",
    "corsheaders",
    "django_extensions",
    "django_filters",
    "drf_spectacular",
    "rest_framework",
    "rest_framework_simplejwt",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if MODE in ["PRODUCTION", "MIGRATE"]:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"

if MODE in ["PRODUCTION", "MIGRATE"]:
    CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    MEDIA_URL = "/media/"
else:
    MY_IP = os.getenv("MY_IP", "127.0.0.1")
    MEDIA_URL = f"http://{MY_IP}:19003/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "core.User"

REST_FRAMEWORK = {
    # "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.DjangoModelPermissions",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 10,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "<PROJETO> API",
    "DESCRIPTION": "API para o projeto <descreva aqui seu projeto>.",
    "VERSION": "1.0.0",
}

print(f"MODE: {MODE} \nMEDIA_URL: {MEDIA_URL} \nDATABASE: {DATABASES}")
