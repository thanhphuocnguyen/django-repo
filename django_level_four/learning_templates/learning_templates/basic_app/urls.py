from django.urls import path
from basic_app.views import other_page, index, relative_page

app_name = 'basic_app'

urlpatterns = [
    path('other/', other_page, name='other'),
    path('relative-page/', relative_page, name='relative'),
]
