from django.urls import path

from contents.views import ContentsDetailAPI, ContentsCreateAPI

urlpatterns = [
    path('', ContentsCreateAPI.as_view()),
    path('/<int:contents_id>', ContentsDetailAPI.as_view())
]
