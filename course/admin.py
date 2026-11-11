from django.contrib import admin
from .models import Student, Teacher, Subject

def new_yosh(modeladmin, request, queryset):
    queryset.update(age=50)
def sertifikat(modeladmin, request, queryset):
    queryset.update(sertifikat=True)
def off(modeladmin, request, queryset):
    queryset.update(sertifkat=False)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', )
    # list_display_links = ('last_name', 'first_name', 'age')
    # readonly_fields = ('age',)
    # ordering = ('first_name', 'last_name',)
    list_filter = ('last_name', 'first_name', 'age',)
    search_fields = ('first_name', 'last_name',)
    actions = (new_yosh,)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sertifikat')
    list_filter = ('last_name', 'first_name',)
    list_display_links = ('last_name', 'first_name', 'sertifikat')
    readonly_fields = ('sertifikat',)
    ordering = ('first_name', 'sertifikat',)
    search_fields = ('first_name', 'last_name',)
    actions = (sertifikat,off)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'student')
    autocomplete_fields = ('student',)
