from django.conf.urls import patterns, url
from myblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<postId>\d+)/$', views.detail, name='detail'),
    url(r'^addpost/', views.newPost, name='newPost'),
    url(r'^createPost/', views.createPost, name='createPost'),
    url(r'^createComment/', views.createComment, name='createComment'),    
)