from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'moreh.views.home', name='home'),
    url(r'^$', 'hebrew_quiz.views.index', name='index'),
    # url(r'^moreh/', include('moreh.foo.urls')),
	url(r'^hebrew_quiz/', include('hebrew_quiz.urls', namespace='hebrew_quiz')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
