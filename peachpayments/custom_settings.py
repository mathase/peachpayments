import os

SLACK_CHANNEL = 'transactions'

PEACH_USER_ID = os.environ.get('PEACH_USER_ID')
PEACH_PASSWORD = os.environ.get('PEACH_PASSWORD')
PEACH_ENTITY_ID = os.environ.get('PEACH_ENTITY_ID')
PEACH_RESULT_PAGE = os.environ.get('PEACH_RESULT_PAGE')
PEACH_ENTITY_RECURRING_ID = os.environ.get('PEACH_ENTITY_RECURRING_ID')
PEACH_BASE_URL = os.environ.get('PEACH_BASE_URL')

ALLOWED_HOSTS = ['198.211.99.20', 'localhost', '127.0.0.1','127.0.0.1:8000','*']

# aws storage
#AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#AWS_AUTO_CREATE_BUCKET = True
#AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#AWS_S3_REGION_NAME = 'eu-central-1'
# AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
#STATIC_URL = "https://s3.amazonaws.com/{}/".format(AWS_STORAGE_BUCKET_NAME)
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# database:
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': os.environ.get('DATABASE_NAME', 'postgres'),
#        'USER': os.environ.get('DATABASE_USER', 'postgres'),
#        'HOST': os.environ.get('DATABASE_HOST', 'postgres'),
#        'PORT': 5432,
#    }
#}
#db_password = os.environ.get('DATABASE_PASSWORD', False)
#if db_password:
#    DATABASES.get('default').update({'PASSWORD': db_password})

COMMUNICATIONGURU_URL = 'https://communicationguru.appointmentguru.co'
# COMMUNICATIONGURU_URL = 'http://communicationguru'
DEFAULT_FROM_EMAIL = 'support@appointmentguru.co'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'kong_oauth.drf_authbackends.KongDownstreamAuthHeadersAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

if os.environ.get('SENTRY_PUBLIC_KEY') is not None:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    dsn = "https://{}@sentry.io/{}".format(
        os.environ.get("SENTRY_PUBLIC_KEY"),
        os.environ.get("SENTRY_PROJECT_ID"),
    )
    sentry_sdk.init(
        dsn=dsn,
        integrations=[DjangoIntegration()]
    )