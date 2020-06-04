from .base import * # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}


INSTALLED_APPS += [
    'debug_toolbar', # DEBUG APP注册
    'pympler',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',# DEBUG中间件
]

# DEBUG IP 配置
# INTERNAL_IPS = ['127.0.0.1']

# DEBUG CONFIG
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
}

# DEBUG PANEL 配置
DEBUG_TOOLBAR_PANELS = [
    #'djdt_flamegraph.FlamegraphPanel',
    'pympler.panels.MemoryPanel',
]
