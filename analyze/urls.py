from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='analyze-home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', extra_context={'group': 'instructor', 'module': 'analyze'}, next_page='../'), name='analyze-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loggedout.html', extra_context={'module': 'analyze'}), name='analyze-logout'),
    path('demo-courses-vs-marks-plot/', views.get_demo_courses_vs_marks_plot),
    path('demo-question-categories-vs-marks-plot/', views.get_demo_question_categories_vs_marks_plot),
    path('demo-time-taken-vs-marks-plot/', views.get_demo_time_taken_vs_marks_plot),
    path('demo-incidents-vs-marks-plot/', views.get_demo_incidents_vs_marks_plot)
]
