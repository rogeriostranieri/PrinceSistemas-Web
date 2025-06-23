"""
Django settings for PrinceSistemas project.
"""
import os
from pathlib import Path

# Tentar importar decouple, se não conseguir usar os.getenv
try:
    from decouple import config
except ImportError:
    def config(key, default=None, cast=None):
        """Fallback se decouple não estiver instalado"""
        value = os.getenv(key, default)
        if cast and value is not None:
            if cast == bool:
                return value.lower() in ('true', '1', 'yes', 'on')
            return cast(value)
        return value

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔧 CONFIGURAÇÃO AMBIENTE usando .env
PRODUCTION = config('PRODUCTION', default=False, cast=bool)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default="django-insecure-&p&lwl)==&6cu$43bj$2!zmt$!ag578$cquy79g5@!w68kk8--")

# 🔒 CONFIGURAÇÕES DE SEGURANÇA E DEBUG HÍBRIDAS
if PRODUCTION:
    DEBUG = False  # 🚨 SEMPRE False em produção
    SECURE_SSL_REDIRECT = False  # 🔧 False para permitir HTTP local
    SESSION_COOKIE_SECURE = False  # 🔧 False para funcionar sem HTTPS local
    CSRF_COOKIE_SECURE = False    # 🔧 False para funcionar sem HTTPS local
    SECURE_HSTS_SECONDS = 0       # 🔧 Desabilitado para ambiente híbrido
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    
    # 🌐 HOSTS PERMITIDOS - HÍBRIDO (LOCAL + EXTERNO)
    ALLOWED_HOSTS = [
        # IPs e domínios externos
        #'189.46.94.184',
        'princesistemas.ddns.net',
        'www.princesistemas.ddns.net',
        # IPs locais
        'localhost',
        '127.0.0.1',
        '0.0.0.0',
        # Rede local  
        '192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5',
        '10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5',
        # '*'  # 🚨 REMOVER temporariamente para teste
    ]
else:
    DEBUG = True
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 0
    
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
       # '189.46.94.184',
        'princesistemas.ddns.net',
        '*'  # Desenvolvimento
    ]

# Configurações adicionais de segurança (sempre ativas)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'corsheaders',
    
    # Apps do projeto
    'apps.login',
    'apps.empresas',
    'apps.laudos',
    'apps.socios',
    'apps.parcelamentos',
    'apps.CNAE',
    'apps.EventosEmpresa',
    'apps.NaturezaJuridica',
    'apps.Sites',
    'apps.BrasilDistritos',
    'apps.BrasilEstados',
    'apps.BrasilMunicipios',
    'apps.cadastro_status.apps.CadastroStatusConfig',
    'apps.api_integracoes',
    'apps.contadores',
    'apps.email',
    'apps.TelefoneOrgaoPublico',
    'apps.Contatos',
    'apps.CADSituacaoAlvara',
    'apps.Anotacoes',
]

MIDDLEWARE = [
    'PrinceSistemas.middleware.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 CORS CONFIGURATION HÍBRIDA
if PRODUCTION:
    CORS_ALLOWED_ORIGINS = [
        # HTTPS Externos
        "https://princesistemas.ddns.net",
        "https://www.princesistemas.ddns.net",
        #"https://189.46.94.184",
        # HTTP Locais - FRONTEND ANGULAR
        "http://localhost:4200",      # Angular padrão
        "http://localhost:8765",      # 🆕 SUA PORTA DO FRONTEND
        "http://127.0.0.1:4200",     # Angular padrão
        "http://127.0.0.1:8765",     # 🆕 SUA PORTA DO FRONTEND
        "http://localhost:8000",      # Backend
        "http://127.0.0.1:8000",     # Backend
        # HTTP Externos (para compatibilidade)
        "http://princesistemas.ddns.net",
        "http://princesistemas.ddns.net:8765",  # 🆕 EXTERNO
       # "http://189.46.94.184",
        #"http://189.46.94.184:8765",            # 🆕 EXTERNO
    ]
    CORS_ALLOW_ALL_ORIGINS = False
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:4200",
        "http://localhost:8765",     # 🆕 SUA PORTA DO FRONTEND
        "http://princesistemas.ddns.net:4200",
        "http://princesistemas.ddns.net:8765", # 🆕 SUA PORTA DO FRONTEND
        "https://princesistemas.ddns.net:4200",
        "https://princesistemas.ddns.net:8765", # 🆕 SUA PORTA DO FRONTEND
        "http://127.0.0.1:4200",
        "http://127.0.0.1:8765",     # 🆕 SUA PORTA DO FRONTEND
    ]
    CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

ROOT_URLCONF = "PrinceSistemas.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "PrinceSistemas.wsgi.application"

# 💾 DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='PrinceDB'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='rs755'),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
            'connect_timeout': 10,
        },
    }
}

# Password validation
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
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# 📁 STATIC FILES CONFIGURATION
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 📷 MEDIA FILES CONFIGURATION
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
}

# 📝 LOGGING CONFIGURATION
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {name} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {asctime} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'security.log',
            'formatter': 'verbose',
        },
        'app_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'app.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'middleware': {
            'handlers': ['security_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['app_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# 📧 EMAIL CONFIGURATION
if PRODUCTION:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
    EMAIL_PORT = int(config('EMAIL_PORT', default='587'))
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
