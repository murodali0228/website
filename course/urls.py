from django.urls import path
from .views import (
    HomeView,
    StudentView,
    SubjectView, DetailSubjectView,
    TeacherView, DetailTeacherView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('student/', StudentView.as_view(), name='students'),
    path('subject/', SubjectView.as_view(), name='subjects'),
    path('subject/<int:pk>/', DetailSubjectView.as_view(), name='detail_subject'),
    path('teacher/', TeacherView.as_view(), name='teachers'),
    path('teacher/<int:pk>/', DetailTeacherView.as_view(), name='detail_teacher'),
]