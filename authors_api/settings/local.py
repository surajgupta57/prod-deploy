ALLOWED_HOSTS = []
from .base import *
from .base import env

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-mz&2ih%fu%bgb&0rwiu*wck5-2(71x$#g%jr#5r-!#%lhr8^9x",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_PORT = env("EMAIL_PORT")
# DEFAULT_FROM_EMAIL = "suraj12911@gmail.com"
# DOMAIN = env("DOMAIN")
# SITE_NAME = "Prod Deployment"
