from django.conf.urls import patterns, url
from user_data import views


urlpatterns = [

    url(r'^adduser$', views.add_user, name = 'adduser'),
    url(r'^addservice$', views.add_service, name = 'adduser'),
    # url(r'^user/search$', views.serach_user, name = 'user'),
    url(r'^user/search/+$', views.serach_user_v1, name = 'user'),
    # url(r'^user/(?P<cust_id>[0-9A-Z]{6})$', views.get_bill_history, name = 'user-detail'),
    url(r'^user/search/(?P<cust_id>[0-9A-Z]{6})$', views.get_bill_history_v1, name='user-detail'),
    ]