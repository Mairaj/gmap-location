from django.conf.urls import patterns, include, url
from geomap import settings 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^detail/(?P<each_position_id>\d+)$', 'project.views.detail_info',name ='detail'),
    # url(r'^geomap/', include('geomap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('gmapi.urls.media')), # Use for debugging only.
    (r'^map$', 'project.views.index'),
    (r'^static/(?P<path>)$','django.views.static.serve', {'document_root': ''})
)
if settings.DEBUG:
        urlpatterns += patterns('',
        url(r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
        )
