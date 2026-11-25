from django.shortcuts import render
from django.views import View
from .models import Student, Subject, Teacher


class HomeView(View):
    def get(self, request):
        return render(request,
        'home.html'
        )
class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(
            request,
'student/student.html',
            {
                'students': students,
            }
        )
class SubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(
            request,
            'subject/subject.html',
            {
                'subjects': subjects,
            }
        )
class DetailSubjectView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        return render(
            request,
            'subject/detail_subject.html',
            {
                'subject': subject,
            }
        )
class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(
            request,
            'teacher/teacher.html',
            {
                'teachers': teachers,
            }
        )
class DetailTeacherView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        return render(
            request,
            'teacher/detail_teacher.html',
            {
                'teacher': teacher,
            }
        )