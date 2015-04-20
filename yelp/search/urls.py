from django.conf.urls import url,patterns
from . import search
from . import views

urlpatterns = patterns('search.views',
	url(r'^$',views.index,name='index'),
	url(r'^search-form/$',search.search_form),
	url(r'^search/$',search.search),
	url(r'^search-post/$',search.search_post),
	url(r'^all_business/$', views.all_business, name='all_business'),
	url(r'^results', views.results, name="results"),
)