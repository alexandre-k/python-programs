from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
        url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
        url(r'^logout-then-login', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
        url(r'^dashboard', views.dashboard, name='dashboard'),
        url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
        ]
