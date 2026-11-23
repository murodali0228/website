from django.urls import path
from .views import (
    HomeView,
    StudentView,
    SubjectView,
    TeacherView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('student/', StudentView.as_view(), name='students'),
    path('subject/', SubjectView.as_view(), name='subject'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
]