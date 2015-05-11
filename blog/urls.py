from django.conf.urls import patterns, url
from blog.views import *

urlpatterns = patterns('',
    url(r'^$', BlogView.as_view(), name='blog_index'),
    url(r'^(?P<slug>[-\w]+)/$', BlogPostView.as_view(), name='blog_post_detail'),
)
