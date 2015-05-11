from django.conf.urls import patterns, url

from hebrew_quiz import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^a=(?P<guess>\d+)/$', views.answer, name='answer'),
    url(r'^cat=(?P<cat>\d+)/$', views.setCategory, name='setCategory'),
    url(r'^showCat=(?P<showCat>\d+)/$', views.showCategories, name='showCategories'),
    url(r'^help=(?P<help>\d+)/$', views.showHelp, name='showHelp'),
)
