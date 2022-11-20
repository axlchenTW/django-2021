# Generated by Django 3.2.6 on 2021-09-24 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20210828_0342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': '學校', 'verbose_name_plural': '學校'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '教師', 'verbose_name_plural': '教師'},
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('R', '常態班'), ('E', '美語班'), ('V', '寒暑假班')], default='R', max_length=1, verbose_name='班別'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.teacher', verbose_name='教師'),
        ),
        migrations.AlterField(
            model_name='coursemember',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.course', verbose_name='課程'),
        ),
        migrations.AlterField(
            model_name='coursemember',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.student', verbose_name='學生'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('1', '國小一年級'), ('2', '國小二年級'), ('3', '國小三年級'), ('4', '國小四年級'), ('5', '國小五年級'), ('6', '國小六年級'), ('7', '國中一年級'), ('8', '國中二年級'), ('9', '國中三年級'), ('A', '高中一年級'), ('B', '高中二年級'), ('C', '高中三年級')], max_length=1, verbose_name='年級'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.school', verbose_name='學校'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=1, verbose_name='性別'),
        ),
    ]