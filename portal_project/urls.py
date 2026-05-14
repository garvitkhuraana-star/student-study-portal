from django.contrib import admin
from django.urls import path
from study_hub import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('quiz/<int:quiz_id>/', views.run_quiz, name='run_quiz'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('register/', views.register, name='register'),
]

