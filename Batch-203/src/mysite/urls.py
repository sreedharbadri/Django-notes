from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','blog.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('blog.urls')),
    url(r'^test/',include('test_app.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^$', 'blog.views.hello_world', name='home'),
    # url(r'^test/', 'blog.views.test_hello', name='testhome'),
    # url(r'^testdata/', 'blog.views.testdata', name='testdata'),
]
