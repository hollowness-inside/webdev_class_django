from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, "web_2025/index.html")

def register(request):
    return render(request, "web_2025/register.html")

def about(request):
    return render(request, "web_2025/about.html")

def feedback(request):
    return render(request, "web_2025/feedback.html")


class StudentProfileView(View):
    def get(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')

        if student_id > 100:
            return Http404("Student not found")

        return HttpResponse(f"Student profile with id {student_id}")


class CourseView(View):
    def get(self, request, *args, **kwargs):
        course_slug = self.kwargs.get('course_slug')

        if len(course_slug) >= 10:
            return Http404("Course not found")

        return render(request, "course.html", context={"course_slug": course_slug})
