from django.conf.urls import patterns, include, url
from django.contrib import admin

import search.views
import search.search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yelp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^search/$',include('search.urls', namespace="search")),
	url(r'^search/$',search.search.search),
	url(r'^search-form/$',search.search.search_form),
	url(r'^search-post/$',search.search.search_post),
	url(r'^$', search.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
