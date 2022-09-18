from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateCarView.as_view(), name='get_or_create'),
    path('<int:pk>',
         views.UpdateDeleteCarView.as_view(),
         name='update_or_delete'),
]
