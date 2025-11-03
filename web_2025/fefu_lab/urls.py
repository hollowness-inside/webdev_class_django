from django.urls import path

from . import views
from .views import CourseView

handler404 = "fefu_lab.views.custom_404_view"

urlpatterns = [
    path("", views.index, name="index"),
    path("feedback/", views.feedback, name="feedback"),

    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    
    path("about/", views.about, name="about"),
    path("student/<int:student_id>/",
         views.student_profile, name="student_profile"),
         
    path("course/<slug:course_slug>/",
         CourseView.as_view(), name="course")
]
