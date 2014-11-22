from django.conf.urls import patterns, include, url
from django.contrib import admin
import django.conf.urls
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TimetableWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', views.main),
)
urlpatterns += patterns('event.views',
    (r'^add_event/$', 'add_event'),
)
