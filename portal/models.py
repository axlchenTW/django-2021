from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class School(models.Model):
    name = models.CharField('學校名稱', max_length=20, db_index=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '學校'
        verbose_name_plural = '學校'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField('教師姓名', max_length=20, db_index=True)
    phone = models.CharField('連絡電話', max_length=20, db_index=True, null=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '教師'
        verbose_name_plural = '教師'

    def __str__(self):
        return self.name


class Student(models.Model):

    class Sex(models.TextChoices):
        MALE = 'M', _('男')
        FEMALE = 'F', _('女')

    class Grade(models.IntegerChoices):
        M1 = 1, _('國小一年級')
        M2 = 2, _('國小二年級')
        M3 = 3, _('國小三年級')
        M4 = 4, _('國小四年級')
        M5 = 5, _('國小五年級')
        M6 = 6, _('國小六年級')
        J1 = 7, _('國中一年級')
        J2 = 8, _('國中二年級')
        J3 = 9, _('國中三年級')
#        S1 = 10, _('高中一年級')
#        S2 = 11, _('高中二年級')
#        S3 = 12, _('高中三年級')

    name = models.CharField('學生姓名', max_length=20, db_index=True)
    sex = models.CharField('性別', max_length=1, choices=Sex.choices, default=Sex.MALE)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='學校')
    grade = models.IntegerField('年級', choices=Grade.choices, default=Grade.M1)
    parent = models.CharField('家長姓名', max_length=20, null=True)
    phone = models.CharField('連絡電話(H)', max_length=20, null=True, blank=True)
    phone2 = models.CharField('連絡電話(O)', max_length=20, null=True, blank=True)
    phone3 = models.CharField('連絡電話(M)', max_length=20, null=True, blank=True)
    phone4 = models.CharField('連絡電話(F)', max_length=20, null=True, blank=True)
    address = models.CharField('地址', max_length=255, null=True, blank=True)
    memo = models.CharField('備註', max_length=40, null=True, blank=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '學生'
        verbose_name_plural = '學生'

    def __str__(self):
        return self.name


class Course(models.Model):

    class CourseType(models.TextChoices):
        REGULAR = 'R', _('常態班')
        ENGLISH = 'E', _('美語班')
        VACATION = 'V', _('寒暑假班')

    name = models.CharField('班級名稱', max_length=40, db_index=True)
    course_type = models.CharField('週期別', max_length=1, choices=CourseType.choices, default=CourseType.REGULAR)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='教師')
    tuition = models.IntegerField('學費', null=True, blank=True)
    meterial_fee = models.IntegerField('材料費', null=True, blank=True)
    start_with = models.DateField('開始日期', null=True, blank=True)
    end_with = models.DateField('結束日期', null=True, blank=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '班級'
        verbose_name_plural = '班級'

    def __str__(self):
        return self.name


class CourseMember(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='班級')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='學生')
    adjustment = models.IntegerField('費用調整', null=True, blank=True)
    memo = models.CharField('備註', max_length=40, null=True, blank=True)

    is_acvite = models.BooleanField('啟用', default=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '班級名單'
        verbose_name_plural = '班級名單'

    def __str__(self):
        return f"{self.course.name} : {self.student.name}"

