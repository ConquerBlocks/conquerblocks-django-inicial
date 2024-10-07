from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "biblioteca" / "templates"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-hb_#nueyw^t-jamukc@)lvqq1%%u0p_fze2+jy^^0sw0_f2$d+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "django_extensions",
    "import_export",
    "rosetta",
    "modeltranslation",
    "books",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',  # Asegúrate de que esté antes de CSRF y después de SessionMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "books.custom_middleware.TiempoDeProcesamientoMiddleware"
]

ROOT_URLCONF = "biblioteca.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATES_DIR,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n", # Añadido para disponer de LANGUAGES en las plantillas
                "biblioteca.context_processor.get_current_year_context_processor",
                "biblioteca.context_processor.get_statistics_books",
            ],
        },
    },
]

WSGI_APPLICATION = "biblioteca.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mydb',                      # Nombre de la base de datos
#         'USER': 'django_user_db',             # Usuario creado para la base de datos
#         'PASSWORD': 'django_user_pass',       # Contraseña del usuario
#         'HOST': '127.0.0.1',                  # Dirección IP del host (localhost o la IP de tu máquina)
#         'PORT': '3306',                       # Puerto por defecto de MySQL
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         }
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

TIME_ZONE = "Europe/Madrid"
USE_I18N = True
USE_L10N = True
USE_TZ = True
PREFIX_DEFAULT_LANGUAGE = True

LANGUAGE_CODE = 'es'  # Idioma predeterminado
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español'),
]

LANGUAGE_COOKIE_NAME = 'django_language'  # Este es el valor por defecto, lo puedes personalizar si lo necesitas

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
MODELTRANSLATION_LANGUAGES = ('es', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('es', )
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'es'


# Definir la ruta donde se almacenarán los archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / 'locale',  # 'locale' será la carpeta donde se guardarán las traducciones
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


INTERNAL_IPS = [
    "127.0.0.1",
]
