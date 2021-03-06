from django.conf import settings
from django.conf.urls.defaults import handler500, handler404, patterns, include, \
    url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog')
)

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)