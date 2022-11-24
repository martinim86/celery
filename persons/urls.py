from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.contacts_view, name='contacts'),
    url('success', views.success_view, name='success'),

]