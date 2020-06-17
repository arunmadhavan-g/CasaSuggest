from django.conf.urls import url
from CasaSuggestApp import views

urlpatterns = [
    url(r'^api/campaign$', views.campaigns),
    url(r'^api/campaign/(?P<campaign_id>[0-9]+)/messages$', views.handle_messages),
    url(r'^api/campaign/(?P<campaign_id>[0-9]+)/messages/(?P<customer_dd>[0-9]+)$', views.tutorial_list_published)
]
