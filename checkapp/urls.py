from django.conf.urls import url
from checkapp import views
urlpatterns = [
    url(r'^$',views.index, name='index'),
]