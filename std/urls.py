from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("home/", home),
    path("add-std/", std_add),
    path("std-delete/<int:roll>", std_delete),
    path("std-update/<int:roll>", std_update),
    path("do-std-update/<int:roll>", do_std_update, name="update_student"),
]
