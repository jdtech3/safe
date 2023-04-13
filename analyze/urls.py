from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='analyze-home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', extra_context={'group': 'instructor', 'module': 'analyze'}, next_page='../'), name='analyze-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loggedout.html', extra_context={'module': 'analyze'}), name='analyze-logout'),
    path('demo-plot/<slug:plot>/', views.get_demo_plot),
]
