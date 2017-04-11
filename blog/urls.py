from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#from In_Store.blog import views as core_views

urlpatterns = [
     url(r'^$', auth_views.login, name='home'),
    #     url(r'^$', views.post_list, name='post_list'),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^accounts/', include('allauth.urls'), name='facebook'),
    url(r'^login/$', auth_views.login, name='home'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', views.home, name='home'),

]