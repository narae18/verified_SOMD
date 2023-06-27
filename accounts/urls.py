from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
    path("login/", login, name="login"),
    path("firstlogin/", dgupass_process, name="firstlogin"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
    path('deleteUser/',deleteUser, name="deleteUser"),
    path("needTologin/",needTologin, name="needTologin"),
    
]