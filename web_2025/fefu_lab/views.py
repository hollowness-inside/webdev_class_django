from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return HttpResponse("Hello, World from a function-based view")


class StudentProfileView(View):
    def get(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')

        if student_id > 100:
            return Http404("Student not found")

        return HttpResponse(f"Student profile with id {student_id}")
