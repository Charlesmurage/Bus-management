from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^findbus/$', views.findbus, name="findbus"),
    url(r'^pay/$', views.pay, name="payment"),
    url(r'^bookings/$', views.bookings, name="bookings"),
    url(r'^cancellings/$', views.cancellings, name="cancellings"),
    url(r'^seebookings/$', views.seebookings, name="seebookings"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'success/$', views.success, name="success"),
    url(r'access/token$', views.getAccessToken, name='get_mpesa_access_token'),
    url(r'online/lipa$', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

    url('signout', views.signout, name="signout"),

]
