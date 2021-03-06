# Generated by Django 3.2.6 on 2021-09-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20210924_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meterial_fee',
            field=models.IntegerField(null=True, verbose_name='材料費'),
        ),
        migrations.AddField(
            model_name='course',
            name='tuition',
            field=models.IntegerField(null=True, verbose_name='學費'),
        ),
        migrations.AddField(
            model_name='coursemember',
            name='adjustment',
            field=models.IntegerField(null=True, verbose_name='費用調整'),
        ),
        migrations.AddField(
            model_name='coursemember',
            name='memo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='備註'),
        ),
        migrations.AddField(
            model_name='school',
            name='is_acvite',
            field=models.BooleanField(default=True, verbose_name='啟用'),
        ),
        migrations.AddField(
            model_name='student',
            name='memo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='備註'),
        ),
        migrations.AddField(
            model_name='student',
            name='parent',
            field=models.CharField(max_length=20, null=True, verbose_name='家長姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(choices=[('1', '國小一年級'), ('2', '國小二年級'), ('3', '國小三年級'), ('4', '國小四年級'), ('5', '國小五年級'), ('6', '國小六年級'), ('7', '國中一年級'), ('8', '國中二年級'), ('9', '國中三年級')], default='1', verbose_name='年級'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='連絡電話(H)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='連絡電話(O)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='連絡電話(M)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone4',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='連絡電話(F)'),
        ),
    ]
