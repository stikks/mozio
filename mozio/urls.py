from django.conf.urls import patterns, include, url

urlpatterns =[
    url(r'^api_auth/', include('rest_framework.urls'), name='rest-framework'),
    url(r'^api/v1/', include('app.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
