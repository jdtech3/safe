from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import SafetyQuizForm

# [/]: home
@login_required(login_url=reverse_lazy('evaluate-login'))
def index(request):
    return render(request, 'evaluate/index.html', {'name': f'{request.user.first_name} {request.user.last_name}'})

# [/quiz/]: safety quiz
@login_required(login_url=reverse_lazy('evaluate-login'))
def get_safety_quiz(request):
    if request.method == 'POST':
        form = SafetyQuizForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('evaluate-thanks'))
        
    else:
        form = SafetyQuizForm()
    
    return render(request, 'evaluate/quiz.html', {'form': form})

# [/thanks/]: safety quiz submitted
def thanks(request):
    return render(request, 'evaluate/thanks.html')
