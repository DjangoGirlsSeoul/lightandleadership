from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^ourstory$', views.our_story, name='our_story'),
    url(r'^ourteam$', views.our_team, name='our_team'),
    url(r'^childrensprogram$', views.childrens_program, name='childrensprogram'),
]