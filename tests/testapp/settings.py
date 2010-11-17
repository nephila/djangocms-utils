

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

CACHE_BACKEND = 'locmem:///'

MANAGERS = ADMINS

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cms.sqlite',
        'TEST_CHARSET': 'utf-8',
        'TEST_COLLATION': 'utf8_general_ci',
        'SUPPORTS_TRANSACTIONS': True
    }
}

TIME_ZONE = 'America/Chicago'

SITE_ID = 1

USE_I18N = True

SECRET_KEY = '*xq7m@)*fpionlm!spa0(jibsrz9%c0d=e(g)v*!17y(vx0ue_3'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.core.context_processors.csrf',
    "cms.context_processors.media",
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    
)

ROOT_URLCONF = 'testapp.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'cms',
    'publisher',
    'menus',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.teaser',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'cms.plugins.inherit',
    'mptt',
    'testapp',
    'djangocms_utils'
)

gettext = lambda s: s

LANGUAGE_CODE = "en"

LANGUAGES = (
    ('fr', gettext('French')),
    ('de', gettext('German')),
    ('en', gettext('English')),
    ('pt-BR', gettext("Brazil")),
)

CMS_LANGUAGE_CONF = {
    'de':['fr', 'en'],
    'en':['fr', 'de'],
}

CMS_TEMPLATES = (
    ('col_two.html', gettext('two columns')),
    ('col_three.html', gettext('three columns')),
    ('nav_playground.html', gettext('navigation examples')),
)

CMS_SOFTROOT = True
CMS_MODERATOR = True
CMS_PERMISSION = True
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_FLAT_URLS = False
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = False
CMS_URL_OVERWRITE = True


