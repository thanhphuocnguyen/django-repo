from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostView.as_view(), name='post_list'),
    url(r'post/(?P<pk>\d+)$',
        views.PostDetailView.as_view(),
        name='post_detail'),
    url(r'post/(?P<pk>\d+)/edit/$',
        views.UpdatePostView.as_view(),
        name='post_update'),
    url(r'post/(?P<pk>\d+)/remove/$',
        views.DeletePostView.as_view(),
        name='post_delete'),
    url(r'post/(?P<pk>\d+)/comment/$',
        views.add_comment_to_post,
        name='post_comment'),
    url(r'post/(?P<pk>\d+)/publish/$', views.post_publish,
        name='post_publish'),
    url(r'comment/(?P<pk>\d+)/approve/$',
        views.comment_approve,
        name='comment_approve'),
    url(r'comment/(?P<pk>\d+)/remove/$',
        views.comment_remove,
        name='comment_remove'),
    path('post/new/', views.CreatePostView.as_view(), name='post_create'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
]
