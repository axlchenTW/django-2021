from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    name = models.CharField('學校名稱', max_length=20, db_index=True)

    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField('教師姓名', max_length=20, db_index=True)
    phone = models.CharField('連絡電話', max_length=20, db_index=True, null=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField('學生姓名', max_length=20, db_index=True)
    phone = models.CharField('連絡電話', max_length=20, db_index=True)
    address = models.CharField('地址', max_length=255, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.SmallIntegerField('年級', default=0)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name_plural = '學生'
        verbose_name = '學生'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('課程名稱', max_length=40, db_index=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name_plural = '課程'
        verbose_name = '課程'

    def __str__(self):
        return self.name


class CourseMember(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name_plural = '課程名單'
        verbose_name = '課程名單'

    def __str__(self):
        return f"{self.course.name} : {self.student.name}"

