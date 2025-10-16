from django.urls import path

from . import views
from .views import StudentProfileView


urlpatterns = [
    path("", views.index, name="index"),
    path("student/<int:student_id>/",
         StudentProfileView.as_view(), name="student_profile")
]
