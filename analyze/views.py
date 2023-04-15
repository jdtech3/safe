from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_GET

from .forms import AnalyzeForm
from utils import charts

# [/]: home
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
def index(request):
    if request.method == 'POST':
        form = AnalyzeForm(request.POST)
        if form.is_valid():
            return render(request, 'analyze/index.html', {'form': form, 'display_graph': True})
        
    else:
        form = AnalyzeForm()

    return render(request, 'analyze/index.html', {'form': form})

# [/demo-plot]: demo plots
@user_passes_test(lambda user: user.groups.filter(name='instructors').exists(), login_url=reverse_lazy('analyze-login'))
@require_GET
def get_demo_plot(request, plot):
    f = None
    if plot == 'courses-vs-marks':    
        f = charts.demo_courses_vs_marks()
    elif plot == 'question-categories-vs-marks':
        f = charts.demo_question_categories_vs_marks()
    elif plot == 'time-taken-vs-marks':
        f = charts.demo_time_taken_vs_marks()
    elif plot == 'incidents-vs-marks':
        f = charts.demo_incidents_vs_marks()
    
    if f is not None:
        img = f.getvalue()
        return HttpResponse(img, content_type='image/png')
    else:
        return HttpResponseNotFound()
