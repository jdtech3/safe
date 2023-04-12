from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='evaluate-home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', extra_context={'group': 'student', 'module': 'evaluate'}, next_page='../'), name='evaluate-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loggedout.html', extra_context={'module': 'evaluate'}), name='evaluate-logout'),
    path('quiz/', views.get_safety_quiz, name='evaluate-quiz'),
    path('thanks/', views.thanks, name='evaluate-thanks'),
]
