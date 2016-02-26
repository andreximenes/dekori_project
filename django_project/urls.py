from django.conf.urls import patterns, include, url
from django.conf import  settings
from django.contrib import admin
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='index'),
    # INDEX SITE
    url(r'^dekori$', 'core.views.site', name='produtos'),
    url(r'^dekori/sobre', 'core.views.sobre', name='sobre'),
    url(r'^dekori/(?P<opcao_menu>\w+)', 'core.views.menu', name='menu'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


urlpatterns += staticfiles_urlpatterns()