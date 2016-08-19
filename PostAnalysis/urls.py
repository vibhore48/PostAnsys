from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^postanalysis/$', views.postanalysis, name='postanalysis'),
]
