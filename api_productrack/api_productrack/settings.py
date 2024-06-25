import os
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='your_secret_key_here')
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api_productrack_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'api_productrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api_productrack.wsgi.application'

# Firebase credentials
FIREBASE_PROJECT_ID = "product-admin-app-16d8b"
FIREBASE_CLIENT_EMAIL = "firebase-adminsdk-jnseo@product-admin-app-16d8b.iam.gserviceaccount.com"
FIREBASE_PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCOi88ALnuz4Dv6
DIgxy8vXZ4exK4ubfFZ4L1xn2d4juf9nqGp/a0L4+0wq4tOUKP0aQEOz9ciNlzOV
HDQawiw8lp2eM7ALaUV9qs33Yd7lClr6WNELUcjzKgCvR7+jzZyXhMQF1Ogxy+ty
FQhqDxKproaWpXYEJz4QAelJgm4j26XK8Z3xD7B9NvZ3Cb5jtngNlBa+nErvRDzD
8JT+pbMohdXnssp6gsDRmxfttZnj71mU5UMP/+8GTrbx6wp2HIlmu9wfTdxzoC20
sN6dqN7txAk1tU+OgMBofBOpUcDLUQ30OI95MFGiNa90e+I30PwU2lZdb7ctP3Q1
bIuumxEZAgMBAAECgf8DE/3fv91LUXqhQoNdZh1xtmLFcUn4/+3bd5gPuFG6NmIo
STyv5abt4fI+ioF9+LrSB0bHzlXrjwFvc5boh3aVkdI6EnIHJd7MkLaXbqrTyz2d
Us73VNVFS5u23uDcroeLSIJTxRghwa1cXtfmh0wkcXXlkrjcSoHeNfgcJXBPA5k/
LsgB0wRorkXKbry8wZDCkgc1zCsTUQAzl98z1k/jN07ha68JoX0RCz2k0ZjylsNU
zUVXz51vyLawsYtSCMJQxwZZp19Ylnv0zyrmXRsNuLVCxsjZBUe++czMzx1ys5T6
/TNkhknflaTvdT+W3dJst55N5+ufNh9UYsMt4cECgYEAwIwnqi2yOR6sPdvu9bGN
bIovF3wvnLzjkhcDUNEZs3ge99N3QIFaZIr3Z9/5RzFvtMYjVoypFSHuzy2mqV9V
OCBMMWpcMvk7j+9vQNBlRnR2xC22BZh+g2LiE5P6TzFuzjRXMpE+8dnJivsE+u4u
8jq2CCYsGoMDhz+JjerrXlkCgYEAvYVmPpxV111oNOea9rK0IGJI4jM5QGyAVyZE
tmxm0jI7EsiLurAdG34yODG6IMunn/+dpvT5lC7AMjQR1FUvI8fgjjtDQrUOUrhB
58Ig9jSEIsMDNggCN8NIuB/iwqsBHEWg+fNdG7zQcvBMQGo78UN5YLV9A+zIiOON
NwCycMECgYEAn8txG52C3D6laUz+Gq84lEx12oK4rNZh8prgqJBwSO42nSvFOyZe
0zQ1MOLC6R+Q+jC5oRlpNV2M6CmVt9ijS8oaEaSYUcFfeguWg+6vLfJ3okXhWvF8
hSNqRh83y8NVlxH/D7tUxrgcuBeswWcsVOD+svKjBXmXUwYa7Ul5/jkCgYEAhaGE
AG23UU25ZmRQLda/j339qhE4MybOL6T6Gi7BKUDlyk7Bx3bab0JCIsFdXjZ7ESPp
g4mEWWnFdyCj2bXesToEKgW7XVPQr57gSYvmNfO9n80lfHmVJsB5i+pft6df9xFZ
eiSQ6DfwOrsY6Op/LZTIBtqxNY1FsM/SCJBjQYECgYEAkyvPnXbNFvREOrfU056M
ei6QLDtjia0c+TA7d1JbyMwL4FtwlDXNSFxfLTXXS0plTNvwaREGcmGOFR4Mjzbw
Ssq078dfQ752XnGatZ2PMismI75sDxnea4PPUnHbgOfFsd6foyeg6yydsHrxjcGe
QEv3lUoLEs1MUhVzmw/84+8=
-----END PRIVATE KEY-----
"""

CREDENTIAL = credentials.Certificate({
    "type": "service_account",
    "project_id": FIREBASE_PROJECT_ID,
    "private_key_id": "ebf90e51f1cb58d169f3b849ba4bc0c8fc0246b7",
    "private_key": FIREBASE_PRIVATE_KEY,
    "client_email": FIREBASE_CLIENT_EMAIL,
    "client_id": "104396993461119708807",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-jnseo%40product-admin-app-16d8b.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(CREDENTIAL)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8100",  # Adjust as needed for your frontend URL
]

CORS_ALLOW_CREDENTIALS = True  # Allow sending credentials (cookies, tokens)
