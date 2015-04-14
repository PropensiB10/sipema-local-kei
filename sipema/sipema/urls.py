from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'polls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#	url('^popups/', include("popups.urls")),
	url(r'^add/order/$', 'polls.views.addOrder'),
	url(r'^add/user/$', 'polls.views.addUser'),#
	url(r'^add/jadwal/$', 'polls.views.addJadwal'),
	url(r'^add/food/$', 'polls.views.addfood'),
	url(r'^view/food/$', 'polls.views.viewfood'),
	url(r'^view/food/delete/$', 'polls.views.deleteFood'),
	url(r'^view/food/update/$', 'polls.views.updateFood'),
	url(r'^view/user/$', 'polls.views.user'), #
	url(r'^view/jadwal/$', 'polls.views.jadwal_kelas'),
	url(r'^view/order/$', 'polls.views.order'),
)
