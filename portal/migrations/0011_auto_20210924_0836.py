# Generated by Django 3.2.6 on 2021-09-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20210924_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_with',
            field=models.DateField(blank=True, null=True, verbose_name='結束日期'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_with',
            field=models.DateField(blank=True, null=True, verbose_name='開始日期'),
        ),
    ]