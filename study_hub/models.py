from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self): return self.title

class StudyQuiz(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self): return self.name

class StudyQuestion(models.Model):
    quiz = models.ForeignKey(StudyQuiz, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self): return self.content

class Choice(models.Model):
    question = models.ForeignKey(StudyQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

class StudentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(StudyQuiz, on_delete=models.CASCADE)
    points = models.IntegerField()
    total_points = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)