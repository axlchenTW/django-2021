from django.contrib import admin
from portal.models import *


# Register your models here.
# admin.site.register(School)
# admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Course)
admin.site.register(CourseMember)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'school', 'grade', 'updated')
    list_filter = ('school', 'grade')
    ordering = ('name',)
    search_fields = ('name', 'phone')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
