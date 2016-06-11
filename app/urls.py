__author__ = 'stikks'

# import core django modules
from django.conf.urls import include, url

# import thirdparty/extensions
from rest_framework.urlpatterns import format_suffix_patterns

# import application modules
import views

urlpatterns = [
    url(r'^currencies$', views.CurrencyList.as_view(), name='currencies'),
    url(r'^languages$', views.LanguageList.as_view(), name='languages'),
    url(r'^transport-providers$', views.TranportProviderList.as_view(), name='transport-providers'),
    url(r'^transport-providers/(?P<pk>[0-9]+)$', views.TransportProviderDetail.as_view()),
    url(r'^transport-providers/(?P<pk>[0-9]+)/service-areas$', views.ServiceAreaList.as_view(), name='service-areas'),
    url(r'^service-areas/(?P<pk>[0-9]+)$', views.ServiceAreaDetail.as_view()),
    url(r'^', views.api_root),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)