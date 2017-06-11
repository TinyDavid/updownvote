from django.conf.urls import url

from . import views

app_name = 'topic'

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^topic$', views.topic, name='topic'),
]