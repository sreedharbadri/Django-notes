from django.conf.urls import include, url
from django.contrib import admin
#from address.views import hello_world
# bug with 1.8
#from address.views import test_hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'AddressBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld/','address.views.hello_world',name="hello"),
    # url(r'^test_hello/','address.views.test_hello',name='test_hello'),
    url(r'^students/','address.views.address',name='students'),
    url(r'^Dstudents/','address.views.Daddress',name='Dstudents'),
    url(r'^Nstudents/','address.views.Naddress',name='Nstudents'),
]
