from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TimetableWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', views.registration),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', { "template_name": "accounts/login.html" }),
    #url(r'^$', views.main),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login' ),
    url(r'^accounts/profile/$', views.later),
    url(r'^$', views.main),
)
urlpatterns += patterns('event.views',
    url(r'^add_event/$', 'add_event'),
    url(r'^day/(?P<day_iter>\d+)/$', 'day_events'),
    url(r'^event/(?P<cur_id>\d+)/$', 'active_event'),
)
