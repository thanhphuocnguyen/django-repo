app_name = 'basic_app'
from . import views
from django.urls import path
from django.conf.urls import url

app_name = "basic_app"
urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(), name='creates_school'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$',
        views.SchoolUpdateView.as_view(),
        name='update_school'),
    url(r'^delete/(?P<pk>\d+)/$',
        views.DeleteView.as_view(),
        name='delete_school'),
]
