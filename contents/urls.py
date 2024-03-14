from django.urls import path

from contents.views import ContentsDetailAPI, ContentsListCreateAPI

urlpatterns = [
    path('', ContentsListCreateAPI.as_view()),
    path('/<int:contents_id>', ContentsDetailAPI.as_view())
]
