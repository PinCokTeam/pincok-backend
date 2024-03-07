from django.urls import path

from member.views import MemberListAPI, MemberDetailAPI

urlpatterns = [
    path('', MemberListAPI.as_view()),
    path('<int:id_>/', MemberDetailAPI.as_view()),
]
