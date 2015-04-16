from django.conf.urls import url

from owc_fixtureless import views

urlpatterns = [
    url(r'^', views.MageView.as_view(), name='mage_index'),
]
