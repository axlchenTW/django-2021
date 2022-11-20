from django.contrib import admin
from portal.models import *

# customize title
admin.site.index_title = "answer admin"
admin.site.site_header = "answer"
admin.site.site_title = "answer workshop"

# Register your models here.
# admin.site.register(School)
# admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Course)
# admin.site.register(CourseMember)

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
    search_fields = ('name', 'phone',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_type', 'teacher', 'tuition', 'meterial_fee')
    ordering = ('name',)
    list_filter = ('course_type',)

@admin.register(CourseMember)
class CourseMemberAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'get_tuition', 'adjustment', 'memo')
    ordering = ('course', 'student',)
    list_filter = ('course','student',)

    @admin.display(description='學費')
    def get_tuition(self, obj):
        return obj.course.tuition
    
