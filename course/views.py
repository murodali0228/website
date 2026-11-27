from django.db.models import Q
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
        search = request.GET.get('search', '')
        if search:
            students = Student.objects.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search)
            )
        else:
            students = Student.objects.all()
        return render(
            request,
'student/student.html',
            {
                'students': students,
                'search': search,
            }
        )
class SubjectView(View):
    def get(self, request):
        search = request.GET.get('search', '')
        if search:
            subjects = Subject.objects.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search)
            )
        else:
            subjects = Subject.objects.all()
        return render(
            request,
            'subject/subject.html',
            {
                'subjects': subjects,
                'search': search,
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