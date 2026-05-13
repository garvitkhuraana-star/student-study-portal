from django.contrib import admin
from django.urls import path
from study_hub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('quiz/<int:quiz_id>/', views.run_quiz, name='run_quiz'),
]