from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('',mainpage, name="mainpage"),
    path('board/',board,name="board"),
    path('register/',register,name="register"),
    path('mysomd/',mysomd,name="mysomd"),
    path('createSOMD/',createSOMD,name="createSOMD"),
    path('mainfeed/<int:id>',mainfeed,name="mainfeed"),
    path('mainfeed/<int:somd_id>/new/',new, name="new"),
    path('mainfeed/<int:somd_id>/createpost/',createpost,name="createpost"),
    path('mainfeed/viewpost/<int:post_id>',viewpost,name="viewpost"),
]