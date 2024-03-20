from django.urls import path
from crew.views import CrewListAPI, CrewDetailAPI

urlpatterns = [
    path('', CrewListAPI.as_view()),
    path('<int:crew_id>', CrewDetailAPI.as_view())
]