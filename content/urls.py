from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^ourstory$', views.our_story, name='our_story'),
]