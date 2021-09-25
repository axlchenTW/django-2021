# Generated by Django 3.2.6 on 2021-09-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20210924_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meterial_fee',
            field=models.IntegerField(blank=True, null=True, verbose_name='材料費'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tuition',
            field=models.IntegerField(blank=True, null=True, verbose_name='學費'),
        ),
        migrations.AlterField(
            model_name='coursemember',
            name='adjustment',
            field=models.IntegerField(blank=True, null=True, verbose_name='費用調整'),
        ),
    ]
