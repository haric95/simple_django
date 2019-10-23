from django.urls import path

from .views import post_list, post_detail, post_create, post_delete, post_update

urlpatterns = [
    path("", post_list),
    path("create/", post_create),
    path("<id>/", post_detail),
    path("<id>/update", post_update),
    path("<id>/delete", post_delete),
]