from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path("mypage/", mypage, name="mypage"),
    path("mypage_edit/", mypage_edit, name="mypage_edit"),
    path("mypage_update/", mypage_update, name="mypage_update"),
]
