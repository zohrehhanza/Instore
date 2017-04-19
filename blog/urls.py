from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
         #     url(r'^$', views.post_list, name='post_list'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^accounts/', include('allauth.urls'), name='facebook'),
    url(r'^login/$', auth_views.login, name='home'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^$', views.home, name='home'),
    #url(r'^accounts/profile', views.home, name='home'),
   # url(r'^accounts/profile/?search_box=(\d+)', views.search_result, name='search_result'),

]
