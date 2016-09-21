from django.conf.urls import patterns, url
from user_data import views
from django.views.generic import RedirectView

urlpatterns = [

    url(r'^adduser$', views.add_user, name = 'adduser'),
    url(r'^addservice/(?P<cust_id>[0-9A-Z]{6})$', views.add_service, name = 'adduser'),
    url(r'^addservice/(?P<cust_id>[0-9A-Z]{6})/(?P<id>[0-9]*)$', views.add_service, name = 'adduser2'),
    # url(r'^user/search$', views.serach_user, name = 'user'),
    url(r'^search/+$', views.serach_user_v1, name = 'user'),
    # url(r'^user/(?P<cust_id>[0-9A-Z]{6})$', views.get_bill_history, name = 'user-detail'),
    url(r'^search/(?P<cust_id>[0-9A-Z]{6})$', views.get_bill_history_v1, name='user-detail'),
    url(r'', RedirectView.as_view(url='/search/')),
    ]