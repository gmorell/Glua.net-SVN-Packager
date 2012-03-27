from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
if not settings.DEBUG:
    handler404 = "glua.error_views.http404"
urlpatterns = patterns('',
    # Example:
    # (r'^glua/', include('glua.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r"^common/(?P<path>.*)$", "django.views.static.serve",
    {"document_root": getattr(settings, "STATIC_DOC_ROOT"),
	    "show_indexes": True}),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$','glua.news.views.index'), # site index
    (r'^news/$','glua.news.views.listnews'),
    (r'^news/(?P<news_slug>[a-zA-Z_-]+)/','glua.news.views.news'),
    (r'^dls/$','glua.svn.views.index'), # download page index
    (r'^dls/std/(?P<fileid>[0-9]+)/','glua.balancer.views.standard'),
    (r'^dls/seed/(?P<fileid>[0-9]+)/','glua.balancer.views.seeds'),
    (r'^seeds/$','glua.svn.views.seeds'),
    (r'^about/$','glua.news.views.about'),
    (r'^donate/$','glua.news.views.donate'),
    (r'^mirrors/$','glua.balancer.views.mirrorlist'),
    (r'^legal/$','glua.news.views.legal'),
    (r'^op/$', 'django.views.generic.simple.direct_to_template', {'template': 'otherprojects.html'}),
)
