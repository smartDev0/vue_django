from django.conf.urls import url
from vue_app import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^employee$',views.tweetApi),
    url(r'^employee/([0-9]+)$',views.tweetApi),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)