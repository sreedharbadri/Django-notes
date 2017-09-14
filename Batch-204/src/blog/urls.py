from django.conf.urls import include, url
from .views import Hello,TestHello


urlpatterns = [
    url(r'^$', Hello, name='Hello'),
    url(r'^test/', TestHello, name='Hello'),
]