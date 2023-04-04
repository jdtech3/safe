from django.shortcuts import render
from django.http import HttpResponse

from utils import charts

# [/]: home
def index(request):
    plot = charts.demo_courses_vs_marks()

    return render(request, 'analyze/index.html')

# [/demo-courses-vs-marks-plot]: demo plot 1
def get_demo_courses_vs_marks_plot(request):
    f = charts.demo_courses_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')

# [/demo-question-categories-vs-marks-plot]: demo plot 2
def get_demo_question_categories_vs_marks_plot(request):
    f = charts.demo_question_categories_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')

# [/demo-time-taken-vs-marks-plot]: demo plot 3
def get_demo_time_taken_vs_marks_plot(request):
    f = charts.demo_time_taken_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')

# [/demo-incidents-vs-marks-plot]: demo plot 4
def get_demo_incidents_vs_marks_plot(request):
    f = charts.demo_incidents_vs_marks()
    img = f.getvalue()

    return HttpResponse(img, content_type='image/png')
