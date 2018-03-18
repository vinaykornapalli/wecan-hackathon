from django.conf.urls import url
from . import  views

app_name = 'post'

urlpatterns = [
    url(r'^$',views.PostListAll.as_view(template_name="post_list.html"),name="all"),
    url(r'new/$',views.CreatePost.as_view(template_name="form_post.html"),name = "create"),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(template_name="post_detail.html"),name="single"),
    url(r'delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name="delete"),


]