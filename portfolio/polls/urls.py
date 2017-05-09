from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', polls.views, name='index'),
    url(r'^admin/', admin.site.urls),
]
