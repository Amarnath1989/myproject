from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.login_view, name='login'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^delete/(?P<resepi_id>\d+)/$', views.delete_resepi, name='detail'),
    url(r'^create/', views.create_resepi, name='create'),
    url(r'^register/', views.user_creation, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
]
