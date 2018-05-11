from .base import *

ALLOWED_HOSTS = ['*']

STATIC_URL='/static/'
STATIC_ROOT=os.path.join(LIVE_DIR, 'static')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(LIVE_DIR, 'media')
