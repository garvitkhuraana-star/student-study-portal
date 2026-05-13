from django.contrib import admin
from .models import Subject, StudyQuiz, StudyQuestion, Choice, StudentRecord

# This allows you to see and edit your study portal data
admin.site.register(Subject)
admin.site.register(StudyQuiz)
admin.site.register(StudyQuestion)
admin.site.register(Choice)
admin.site.register(StudentRecord)