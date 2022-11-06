# Copyright (c) 2021 Jonathan Vice

from django.urls import path

from . import views

app_name = "scheduler"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add-room", views.add_room, name="add_room"),
    path("add-event", views.add_event, name="add_event"),
    path("del_room", views.del_room, name="del_room"),
    path("edit_event", views.edit_event, name="edit_event"),
]
