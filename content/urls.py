from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ourstory$', views.our_story, name='our_story'),
    url(r'^ourteam$', views.our_team, name='our_team'),
    url(r'^childrensprogram$', views.childrens_program, name='childrensprogram'),
    url(r'^teensprogram$', views.teens_program, name='teensprogram'),
    url(r'^womensprogram$', views.womens_program, name='womensprogram'),
    url(r'^artisanprogram$', views.artisan_program, name='artisanprogram'),
    url(r'^ethics$', views.ethical_post, name='ethical_page'),
    url(r'^peru$', views.why_peru, name='peru'),
    url(r'^volunteerperu$', views.volunteer_peru, name='volunteer_peru'),
    url(r'^financials$', views.financials, name='financials'),
    url(r'^donations$', views.donations, name='donations'),
    url(r'^chicago$', views.volunteer_chicago, name='volunteer_chicago'),
]
