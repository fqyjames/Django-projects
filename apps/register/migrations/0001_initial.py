# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 21:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('gender', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='female', max_length=10)),
                ('nation', models.CharField(choices=[('han', '\u6c49\u65cf'), ('zhuang', '\u58ee\u65cf'), ('man', '\u6ee1\u65cf'), ('hui', '\u56de\u65cf'), ('\u82d7', '\u82d7\u65cf'), ('weiwuer', '\u7ef4\u543e\u5c14\u65cf'), ('tujia', '\u571f\u5bb6\u65cf'), ('yizu', '\u5f5d\u65cf'), ('menggu', '\u8499\u53e4\u65cf'), ('zang', '\u85cf\u65cf'), ('buyizu', '\u5e03\u4f9d\u65cf'), ('dongzu', '\u4f97\u65cf'), ('yaozu', '\u7476\u65cf'), ('chaoxian', '\u671d\u9c9c\u65cf'), ('baizu', '\u767d\u65cf'), ('hanizu', '\u54c8\u5c3c\u65cf'), ('hasakezu', '\u54c8\u8428\u514b\u65cf'), ('lizu', '\u9ece\u65cf'), ('daizu', '\u50a3\u65cf'), ('shezu', '\u7572\u65cf'), ('lisuzu', '\u5088\u50f3\u65cf'), ('gelaozu', '\u4ee1\u4f6c\u65cf'), ('dongxiangzu', '\u4e1c\u4e61\u65cf'), ('gaoshanzu', '\u9ad8\u5c71\u65cf'), ('lahuzu', '\u62c9\u795c\u65cf'), ('shuizu', '\u6c34\u65cf'), ('wazu', '\u4f64\u65cf'), ('naxizu', '\u7eb3\u897f\u65cf'), ('qiangzu', '\u7f8c\u65cf'), ('tuzu', '\u571f\u65cf'), ('mulaozu', '\u4eeb\u4f6c\u65cf'), ('xibozu', '\u9521\u4f2f\u65cf'), ('keerkezizu', '\u67ef\u5c14\u514b\u5b5c\u65cf'), ('dawoerzu', '\u8fbe\u65a1\u5c14\u65cf'), ('jingpozu', '\u666f\u9887\u65cf'), ('maonanzu', '\u6bdb\u5357\u65cf'), ('salazu', '\u6492\u62c9\u65cf'), ('bulangzu', '\u5e03\u6717\u65cf'), ('tajikezu', '\u5854\u5409\u514b\u65cf'), ('achangzu', '\u963f\u660c\u65cf'), ('pumizu', '\u666e\u7c73\u65cf'), ('ewenkezu', '\u9102\u6e29\u514b\u65cf'), ('nuzu', '\u6012\u65cf'), ('jingzu', '\u4eac\u65cf'), ('jinuozu', '\u57fa\u8bfa\u65cf'), ('deangzu', '\u5fb7\u6602\u65cf'), ('baoanzu', '\u4fdd\u5b89\u65cf'), ('eluosizu', '\u4fc4\u7f57\u65af\u65cf'), ('yuguzu', '\u88d5\u56fa\u65cf'), ('wuzibiekezu', '\u4e4c\u5b5c\u522b\u514b\u65cf'), ('menbazu', '\u95e8\u5df4\u65cf'), ('elunchunzu', '\u9102\u4f26\u6625\u65cf'), ('dulongzu', '\u72ec\u9f99\u65cf'), ('tataerzu', '\u5854\u5854\u5c14\u65cf'), ('hezhezu', '\u8d6b\u54f2\u65cf'), ('luobazu', '\u73de\u5df4\u65cf')], default='han', max_length=10, verbose_name='\u6c11\u65cf')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('polity', models.CharField(choices=[('communist', '\u515a\u5458'), ('league', '\u5973'), ('non-communist', '\u515a\u5916\u4eba\u58eb')], default='non-communist', max_length=10)),
                ('expected_salary', models.CharField(max_length=15, verbose_name='\u671f\u671b\u85aa\u8d44')),
                ('marriage', models.CharField(choices=[('single', '\u672a\u5a5a'), ('married', '\u5df2\u5a5a'), ('divorced', '\u79bb\u5f02')], default='single', max_length=15, verbose_name='\u5a5a\u59fb\u72b6\u51b5')),
            ],
            options={
                'verbose_name': '\u57fa\u672c\u4fe1\u606f',
                'verbose_name_plural': '\u57fa\u672c\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfMobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='\u672c\u4eba\u8054\u7cfb\u7535\u8bdd')),
                ('email', models.EmailField(max_length=50, verbose_name='\u90ae\u7bb1')),
                ('emergencyContact', models.CharField(max_length=10, verbose_name='\u7d27\u6025\u8054\u7cfb\u4eba')),
                ('emergencyContactPhone', models.CharField(max_length=11, verbose_name='\u7d27\u6025\u8054\u7cfb\u4eba\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u65b9\u5f0f',
                'verbose_name_plural': '\u8054\u7cfb\u65b9\u5f0f',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('schoolName', models.CharField(max_length=30, verbose_name='\u5b66\u6821\u540d\u79f0')),
                ('major', models.CharField(max_length=20, verbose_name='\u4e13\u4e1a')),
                ('degree', models.CharField(max_length=30, verbose_name='\u6559\u80b2\u7a0b\u5ea6')),
            ],
            options={
                'verbose_name': '\u6559\u80b2\u7ecf\u5386',
                'verbose_name_plural': '\u6559\u80b2\u7ecf\u5386',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('relationship', models.CharField(max_length=10, verbose_name='\u5173\u7cfb')),
                ('organization', models.CharField(max_length=20, verbose_name='\u5355\u4f4d')),
                ('contactPhone', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u5bb6\u5ead\u72b6\u51b5',
                'verbose_name_plural': '\u5bb6\u5ead\u72b6\u51b5',
            },
        ),
        migrations.CreateModel(
            name='IDResidency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNumber', models.CharField(max_length=18, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801')),
                ('idAddress', models.CharField(max_length=100, verbose_name='\u8eab\u4efd\u8bc1\u5730\u5740')),
                ('liveAddress', models.CharField(max_length=100, verbose_name='\u73b0\u4f4f\u5730\u5740')),
                ('origin', models.CharField(max_length=8, verbose_name='\u7c4d\u8d2f')),
                ('houseHoldRegister', models.CharField(choices=[('native', '\u672c\u5e02\u6237\u53e3'), ('non-native_city', '\u975e\u672c\u5e02\u57ce\u9547'), ('non-native_country', '\u975e\u672c\u5e02\u519c\u4e1a')], default='non-native_country', max_length=8, verbose_name='\u6237\u7c4d')),
            ],
            options={
                'verbose_name': '\u8eab\u4efd\u6237\u7c4d\u5730\u5740',
                'verbose_name_plural': '\u8eab\u4efd\u6237\u7c4d\u5730\u5740',
            },
        ),
        migrations.CreateModel(
            name='JobSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internet', models.CharField(max_length=11, verbose_name='\u4e92\u8054\u7f51')),
                ('staffIntroduce', models.CharField(max_length=11, verbose_name='\u5458\u5de5\u4ecb\u7ecd')),
            ],
            options={
                'verbose_name': '\u62db\u8058\u9014\u5f84',
                'verbose_name_plural': '\u62db\u8058\u9014\u5f84',
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signatureId', models.CharField(max_length=20, verbose_name='\u7b7e\u540d\u9a8c\u8bc1\u7801')),
                ('signatureDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u7b7e\u5b57\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7b7e\u540d',
                'verbose_name_plural': '\u7b7e\u540d',
            },
        ),
        migrations.CreateModel(
            name='SkillSpeciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('english', '\u82f1\u8bed'), ('mandarin', '\u666e\u901a\u8bdd'), ('cantonese', '\u7ca4\u8bed')], max_length=10, verbose_name='\u8bed\u8a00')),
                ('computer', models.CharField(max_length=11, verbose_name='\u8ba1\u7b97\u673a')),
            ],
            options={
                'verbose_name': '\u6280\u80fd\u7279\u957f',
                'verbose_name_plural': '\u6280\u80fd\u7279\u957f',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('trainingInstituteName', models.CharField(max_length=30, verbose_name='\u673a\u6784\u540d\u79f0')),
                ('trainingCourse', models.CharField(max_length=30, verbose_name='\u57f9\u8bad\u8bfe\u7a0b')),
                ('certificate', models.CharField(max_length=30, verbose_name='\u8bc1\u4e66\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u57f9\u8bad\u7ecf\u5386',
                'verbose_name_plural': '\u57f9\u8bad\u7ecf\u5386',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('companyName', models.CharField(max_length=30, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('title', models.CharField(max_length=15, verbose_name='\u804c\u4f4d')),
                ('salary', models.CharField(max_length=15, verbose_name='\u85aa\u8d44')),
                ('quitReason', models.CharField(max_length=20, verbose_name='\u79bb\u804c\u539f\u56e0')),
                ('witness', models.CharField(max_length=20, verbose_name='\u8bc1\u660e\u4eba')),
                ('witnessPhone', models.CharField(max_length=11, verbose_name='\u8bc1\u660e\u4eba\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u7ecf\u5386',
                'verbose_name_plural': '\u5de5\u4f5c\u7ecf\u5386',
            },
        ),
    ]