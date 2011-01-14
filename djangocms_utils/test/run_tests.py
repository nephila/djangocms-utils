import sys

def run_tests():
    
    from django.conf import settings
    
    settings.configure(
        DATABASES = {
            'default':  {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'djangocms_utils.db'
            }
        },
        
        TEMPLATE_CONTEXT_PROCESSORS = (
            "django.core.context_processors.auth",
            "django.core.context_processors.i18n",
            "django.core.context_processors.debug",
            "django.core.context_processors.request",
            "django.core.context_processors.media",
            'django.core.context_processors.csrf',
            "cms.context_processors.media",
        ),
        
        
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
            
        ),
        
        ROOT_URLCONF = 'testapp.urls',
        
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
            'mptt',
            'djangocms_utils.test.testapp',
            'djangocms_utils'
        ),
        
        
        LANGUAGE_CODE = "en",
        
        LANGUAGES = (
            ('en', 'English'),
            ('fr', 'French'),
            ('de', 'German'),
        
        ),
        
        CMS_LANGUAGE_CONF = {
            'de':['fr', 'en'],
            'en':['fr', 'de'],
        },
        
        CMS_TEMPLATES = (
            ('col_two.html', 'two columns'),
        ),
        
        CMS_SOFTROOT = True,
        CMS_MODERATOR = True,
        CMS_PERMISSION = True,
        CMS_REDIRECTS = True,
        CMS_SEO_FIELDS = True,
        CMS_FLAT_URLS = False,
        CMS_MENU_TITLE_OVERWRITE = True,
        CMS_HIDE_UNTRANSLATED = False,
        CMS_URL_OVERWRITE = True
    )
    
    from django.test.utils import get_runner

    failures = get_runner(settings)().run_tests(['djangocms_utils'])
    sys.exit(failures)

if __name__ == '__main__':
    run_tests()