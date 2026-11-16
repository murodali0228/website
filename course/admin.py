from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student, Teacher, Subject

def new_yosh(modeladmin, request, queryset):
    queryset.update(age=50)
def sertifikat(modeladmin, request, queryset):
    queryset.update(sertifikat=True)

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'age', )
    list_filter = ('last_name', 'first_name', 'age',)
    search_fields = ('first_name', 'last_name',)
    actions = (new_yosh,)

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'sertifikat')


@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ('subject', 'teacher', 'student')
    autocomplete_fields = ('student',)
