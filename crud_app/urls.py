from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("newpost/", views.new_post, name="newpost"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("editpost/<int:id>/", views.edit_post, name="editpost"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("deletepost/<int:id>/", views.delete_post, name="deletepost"),
]