from django.conf.urls import include, url
from django.contrib import admin
from address.api import AddressResource
address_resource = AddressResource()
from AddressBook.settings.development import DEBUG
from django.views.decorators.cache import cache_page
from address.views import home
#from address.views import hello_world
# bug with 1.8
#from address.views import test_hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'AddressBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),       # Admin page
    url(r'^$', cache_page(60*15)(home), name='home'),   # home page
    # url(r'^helloworld/','address.views.hello_world',name="hello"),  
    # url(r'^test_hello/','address.views.test_hello',name='test_hello'),
    # url(r'^students/','address.views.address',name='students'),
    # url(r'^Dstudents/','address.views.Daddress',name='Dstudents'),
    #url(r'^student_details/','address.views.Naddress',name='student_details'),
    # url(r'^testing_app/','newtest_app.views.Taddress',name='testing_app'),
    # day 7
    url(r'^student_details/',cache_page(60*15)('address.views.Naddress'),name='student_details'),
    #url(r'^contactus/',cache_page(60*15)('address.views.contact'),name="contact"),   # contact page
    url(r'^contactus/','address.views.contact',name="contact"),   # contact page
    url(r'^address/','address.views.address_form',name="address"), # address form
    url(r'^thankyou/','address.views.thank_you',name="thankyou"), #  Thank you form
    url(r'^bootme/','address.views.bootme',name='bootme'),  # testing the bootstrap
    url(r'^accounts/', include('registration.backends.default.urls')), # django-registration redux
    url(r'^api/', include(address_resource.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^local/','address.views.my_function',name="localtest"),
]

if DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
