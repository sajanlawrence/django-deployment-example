from django.conf.urls import  url
from first_app import views

app_name = 'first_app'
urlpatterns = [
    url(r'^register/$',views.signup,name="register"),
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^logout/$',views.user_logout,name="user_logout"),
    url(r'^special/$',views.special,name="special"),
]
