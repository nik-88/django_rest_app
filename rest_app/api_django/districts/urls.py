from django.conf.urls import url
from districts import views

urlpatterns = [
    url(r'^districts/$', views.district_list),
    url(r'^districts/(?P<pk>[0-9]+)/$', views.district_detail),
    url(r'^campuses/$', views.campus_list),
    url(r'^campuses/(?P<pk>[0-9]+)/$', views.campus_detail),
]
