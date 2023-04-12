from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from utils import charts

# [/]: home
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
def index(request):
    plot = charts.demo_courses_vs_marks()

    return render(request, 'analyze/index.html')

# [/demo-courses-vs-marks-plot]: demo plot 1
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
def get_demo_courses_vs_marks_plot(request):
    f = charts.demo_courses_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')

# [/demo-question-categories-vs-marks-plot]: demo plot 2
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
def get_demo_question_categories_vs_marks_plot(request):
    f = charts.demo_question_categories_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')

# [/demo-time-taken-vs-marks-plot]: demo plot 3
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
def get_demo_time_taken_vs_marks_plot(request):
    f = charts.demo_time_taken_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')

# [/demo-incidents-vs-marks-plot]: demo plot 4
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
def get_demo_incidents_vs_marks_plot(request):
    f = charts.demo_incidents_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')
