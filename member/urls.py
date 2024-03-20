from django.urls import path

from member.views import MemberCreateAPI, MemberDetailAPI

urlpatterns = [
    path('', MemberCreateAPI.as_view()),
    path('/<int:member_id>', MemberDetailAPI.as_view())
]
