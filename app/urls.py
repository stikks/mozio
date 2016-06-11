__author__ = 'stikks'

# import core django modules
from django.conf.urls import include, url

# import thirdparty/extensions
from rest_framework.urlpatterns import format_suffix_patterns

# import application modules
from .views import api_root, UserDetail, UserList, LanguageList, CurrencyList, TransportProviderList, \
    TransportProviderDetail, ServiceAreaList, ServiceAreaDetail

urlpatterns = [
    url(r'^currencies$', CurrencyList.as_view(), name='currencies'),
    url(r'^languages$', LanguageList.as_view(), name='languages'),
    url(r'^transport-providers$', TransportProviderList.as_view(), name='transport-providers'),
    url(r'^transport-providers/(?P<pk>[0-9]+)$', TransportProviderDetail.as_view()),
    url(r'^transport-providers/(?P<pk>[0-9]+)/service-areas$', ServiceAreaList.as_view()),
    url(r'^service-areas/(?P<pk>[0-9]+)$', ServiceAreaDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)