from django.conf.urls import url
from . import views
from django.views.generic.list import ListView
from .models import Category

urlpatterns = [
    url(r'^$', ListView.as_view(model=Category, template_name='blog/post_list.html')),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
