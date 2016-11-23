from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from saltweb import views as saltviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'operationplatform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', saltviews.login),
    url(r'^index/$', saltviews.index),
    url(r'^register/$', saltviews.register),
    url(r'^login/$', saltviews.login),
    url(r'^logout/$', saltviews.logout),
    url(r'^createuser/$', saltviews.createuser),
    url(r'^getusername/$', saltviews.getusername),
    url(r'^checkuser/$', saltviews.checkuser),
    url(r'^saltcontrol/$', saltviews.saltcontrol),
    url(r'^cmdhistorylist/$', saltviews.showcmdhistory),
    url(r'^addviews/$', saltviews.addviews),
    url(r'^addcomment/$', saltviews.addcomment),
    url(r'^showcomments/$', saltviews.showcomments),
    url(r'^saltbbs/$', saltviews.saltbbs),
    url(r'^chathome/$', saltviews.chathome),
    url(r'^checkchat/$', saltviews.checkchat),
)
