from django.conf.urls import url, include
from Farmer.views import farmer_list, farm_list, schedule_list

urlpatterns = [
    url(r'^$', farmer_list, name='farmer_list'),
    url(r'^farms/$', farm_list, name='farm_list'),
    url(r'^farms/schedule/$', schedule_list, name='schedule_list'),
    # url(r'^farm-detail/(?P<id>\d+)/$', farm_detail, name='farm_detail'),
    # url(r'^schedules/$', )
]
