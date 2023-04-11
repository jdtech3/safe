from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='analyze-home'),
    path('demo-courses-vs-marks-plot/', views.get_demo_courses_vs_marks_plot),
    path('demo-question-categories-vs-marks-plot/', views.get_demo_question_categories_vs_marks_plot),
    path('demo-time-taken-vs-marks-plot/', views.get_demo_time_taken_vs_marks_plot),
    path('demo-incidents-vs-marks-plot/', views.get_demo_incidents_vs_marks_plot)
]
