from django.http import Http404, HttpResponse
from django.shortcuts import render

from . import forms
from . import constants
from . import models


def index(request):
    total_members = models.Member.objects.filter(is_active=True).count()
    total_volturians = models.Volturian.objects.filter(is_active=True).count()
    total_courses = models.Course.objects.filter(is_active=True).count()
    recent_courses = models.Course.objects.filter(
        is_active=True).order_by('-created_at')[:3]

    return render(request, "web_2025/index.html", context={
        'total_members': total_members,
        'total_volturians': total_volturians,
        'total_courses': total_courses,
        'recent_courses': recent_courses
    })


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Correct")
    else:
        form = forms.RegistrationForm()

    return render(request, 'web_2025/register.html', context={'form': form})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Correct")
    else:
        form = forms.LoginForm()

    return render(request, 'web_2025/login.html', context={'form': form})


def about(request):
    return render(request, "web_2025/about.html")


def feedback(request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponse("Correct")
    else:
        form = forms.FeedbackForm()

    return render(request, 'web_2025/feedback.html', context={'form': form})


CLANS = {
    'CUL': "Олимпийский клан",
    'QUI': "Квидитч клан"
}


def student_profile(request, student_id: int):
    student = models.Member.objects.filter(id=student_id).first()
    if student is not None:
        everyone_else = models.Member.objects.exclude(id=student_id)
        clan = CLANS.get(student.clan, 'Неопознанный клан')
        return render(request, "web_2025/student.html", context={
            "student": student,
            "clan": clan,
            "everyone_else": everyone_else
        })

    students = models.Member.objects.filter(is_active=True)
    return render(request, "web_2025/all_students.html", context={"students": students})


def course(request, course_slug):
    if (context := constants.COURSES_DATA.get(course_slug, None)) is not None:
        return render(request, "web_2025/course.html", context=context)

    return render(request, "web_2025/base-404.html", context={"word": "курса"})
