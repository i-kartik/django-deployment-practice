from django.conf.urls import url
from basic_app import views

#template urls
app_name='basic_app'

urlpatterns=[

    url('register/',views.register,name='register'),
    url('login/',views.user_login,name='userlogin'),

]
