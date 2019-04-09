
from django.conf.urls import url
from django.contrib import admin
from updates.views import ( update_model_detail_view,
                            JsonCBV,
                            JsonCBV2,
                            SerializedListView,
                            SerializedDetailView, )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/$', update_model_detail_view),
    url(r'^json/example1/$', JsonCBV.as_view()),
    url(r'^json/detail/$', SerializedDetailView.as_view()),
    url(r'^json/list/$', SerializedListView.as_view()),
]
