from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from .forms import SafetyQuizForm

# [/]: home
@user_passes_test(lambda user: user.groups.filter(name='students').exists(), login_url=reverse_lazy('evaluate-login'))
def index(request):
    return render(request, 'evaluate/index.html', {'name': f'{request.user.first_name} {request.user.last_name}'})

# [/quiz/]: safety quiz
@user_passes_test(lambda user: user.groups.filter(name='students').exists(), login_url=reverse_lazy('evaluate-login'))
def get_safety_quiz(request):
    # User data
    prefill = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }

    if request.method == 'POST':
        form = SafetyQuizForm(request.POST, initial=prefill)
        if form.is_valid():
            return HttpResponseRedirect(reverse('evaluate-thanks'))
        
    else:
        form = SafetyQuizForm(initial=prefill)
    
    return render(request, 'evaluate/quiz.html', {'form': form})

# [/thanks/]: safety quiz submitted
def thanks(request):
    # TODO: Implement actual autograding feedback
    return render(request, 'evaluate/thanks.html')
