from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.word_list, name='word_list'),
    url(r'^word/new/$', views.word_new, name='word_new'),
]
