from decouple import config
import os

DJANGO_SETTINGS_MODULE=os.environ.get('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE', default='stockintrapal.settings'))
DB_HOST = os.environ.get('DB_HOST', config('DB_HOST', default='127.0.0.1'))
DEBUG = os.environ.get('DEBUG', config('DEBUG', default=False, cast=bool))
WPCUSTOMAPISUBM = os.environ.get('WPCUSTOMAPISUBM', config('WPCUSTOMAPISUBM'))
WPUSER = os.environ.get('WPUSER', config('WPUSER'))
WPPASS = os.environ.get('WPPASS', config('WPPASS'))
SRTOK = os.environ.get('SRTOK', config('SRTOK'))
DB_NAME = os.environ.get('DB_NAME', config('DB_NAME'))
DB_USR = os.environ.get('DB_USR', config('DB_USR'))
DB_PASS = os.environ.get('DB_PASS', config('DB_PASS'))
DB_PORT = os.environ.get('DB_PORT', config('DB_PORT'))
SECRET_KEY = os.environ.get('SECRET_KEY', config('SECRET_KEY'))
APPHOST = os.environ.get('APPHOST', config('APPHOST'))
PRFTAPIKEY = os.environ.get('PRFTAPIKEY', config('PRFTAPIKEY'))
DJANGO_CSRF_ORIGIN = os.environ.get('DJANGO_CSRF_ORIGIN', config('DJANGO_CSRF_ORIGIN', default=''))
DJANGO_ALLOWED_HOST = os.environ.get('DJANGO_ALLOWED_HOST', config('DJANGO_ALLOWED_HOST', default='*'))

frmids = [7, 3, 4, 5]