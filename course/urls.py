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
    path('subject/', SubjectView.as_view(), name='subjects'),
    path('teacher/', TeacherView.as_view(), name='teachers'),
]