from django.http import Http404
from django.shortcuts import render
from django.views import View
from . import constants


def index(request):
    return render(request, "web_2025/index.html")


def register(request):
    return render(request, "web_2025/register.html")


def login(request):
    return render(request, "web_2025/login.html")


def about(request):
    return render(request, "web_2025/about.html")


def feedback(request):
    return render(request, "web_2025/feedback.html")


def feedback(request):
    return render(request, "web_2025/feedback.html")


def student_profile(request, student_id: int):
    if student_id > 100:
        return Http404("Student not found")

    if (context := constants.STUDENTS_DATA.get(student_id, None)) is not None:
        return render(request, "web_2025/student.html", context=context)

    return render(request, "web_2025/student-not-found.html")


class CourseView(View):
    def get(self, request, *args, **kwargs):
        course_slug = self.kwargs.get('course_slug')

        if len(course_slug) >= 10:
            return Http404("Course not found")

        return render(request, "course.html", context={"course_slug": course_slug})
