# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class BasicInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    gender = models.CharField(max_length=10, choices=(('male', u'男'), ('female', u'女')), default='female')
    nation = models.CharField(max_length=10, verbose_name=u'民族', default='han',
                              choices=(('han', u'汉族'), ('zhuang', u'壮族'), ('man', u'满族'),
                              ('hui', u'回族'), ('苗', u'苗族'), ('weiwuer', u'维吾尔族'),
                                       ('tujia', u'土家族'), ('yizu', u'彝族'), ('menggu', u'蒙古族'),
                                       ('zang', u'藏族'), ('buyizu', u'布依族'), ('dongzu', u'侗族'),
                                       ('yaozu', u'瑶族'), ('chaoxian', u'朝鲜族'), ('baizu', u'白族'),
                                       ('hanizu', u'哈尼族'), ('hasakezu', u'哈萨克族'), ('lizu', u'黎族'),
                                       ('daizu', u'傣族'), ('shezu', u'畲族'), ('lisuzu', u'傈僳族'),
                                       ('gelaozu', u'仡佬族'), ('dongxiangzu', u'东乡族'), ('gaoshanzu', u'高山族'),
                                       ('lahuzu', u'拉祜族'), ('shuizu', u'水族'), ('wazu', u'佤族'),
                                       ('naxizu', u'纳西族'), ('qiangzu', u'羌族'), ('tuzu', u'土族'),
                                       ('mulaozu', u'仫佬族'), ('xibozu', u'锡伯族'), ('keerkezizu', u'柯尔克孜族'),
                                       ('dawoerzu', u'达斡尔族'), ('jingpozu', u'景颇族'), ('maonanzu', u'毛南族'),
                                       ('salazu', u'撒拉族'),('bulangzu', u'布朗族'), ('tajikezu', u'塔吉克族'),
                                       ('achangzu', u'阿昌族'), ('pumizu', u'普米族'), ('ewenkezu', u'鄂温克族'), ('nuzu', u'怒族'),
                                       ('jingzu', u'京族'), ('jinuozu', u'基诺族'), ('deangzu', u'德昂族'), ('baoanzu', u'保安族'),
                                       ('eluosizu', u'俄罗斯族'), ('yuguzu', u'裕固族'), ('wuzibiekezu', u'乌孜别克族'),
                                       ('menbazu', u'门巴族'), ('elunchunzu', u'鄂伦春族'), ('dulongzu', u'独龙族'),
                                       ('tataerzu', u'塔塔尔族'), ('hezhezu', u'赫哲族'), ('luobazu', u'珞巴族')))
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    polity = models.CharField(max_length=10, choices=(('communist', u'党员'), ('league', u'女'),
                                                      ('non-communist', u'党外人士')), default='non-communist')
    expected_salary = models.CharField(max_length=15, verbose_name=u'期望薪资')
    marriage = models.CharField(max_length=15, choices=(('single', u'未婚'), ('married', u'已婚'),
                                                      ('divorced', u'离异')), default='single',
                                verbose_name=u'婚姻状况')

    class Meta:
        verbose_name = u'基本信息'
        verbose_name_plural = verbose_name


class IDResidency(models.Model):
    idNumber = models.CharField(max_length=18, verbose_name=u'身份证号码')
    idAddress = models.CharField(max_length=100, verbose_name=u'身份证地址')
    liveAddress = models.CharField(max_length=100, verbose_name=u'现住地址')
    origin = models.CharField(max_length=8, verbose_name=u'籍贯')
    houseHoldRegister = models.CharField(max_length=8, choices=(('native', u'本市户口'), ('non-native_city', u'非本市城镇'),
                                                      ('non-native_country', u'非本市农业')), default='non-native_country',
                                         verbose_name=u'户籍')

    class Meta:
        verbose_name = u'身份户籍地址'
        verbose_name_plural = verbose_name


class Contact(models.Model):
    selfMobile = models.CharField(max_length=11,null=True,blank=True, verbose_name=u'本人联系电话')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    emergencyContact = models.CharField(max_length=10, verbose_name=u'紧急联系人')
    emergencyContactPhone = models.CharField(max_length=11, verbose_name=u'紧急联系人电话')

    class Meta:
        verbose_name = u'联系方式'
        verbose_name_plural = verbose_name


class Education(models.Model):
    startTime = models.DateTimeField(verbose_name=u'开始时间', default=datetime.now)
    endTime = models.DateTimeField(verbose_name=u'结束时间', default=datetime.now)
    schoolName = models.CharField(max_length=30, verbose_name=u'学校名称')
    major = models.CharField(max_length=20, verbose_name=u'专业')
    degree = models.CharField(max_length=30, verbose_name=u'教育程度')

    class Meta:
        verbose_name = u'教育经历'
        verbose_name_plural = verbose_name


class WorkExperience(models.Model):
    startTime = models.DateTimeField(verbose_name=u'开始时间', default=datetime.now)
    endTime = models.DateTimeField(verbose_name=u'结束时间', default=datetime.now)
    companyName = models.CharField(max_length=30, verbose_name=u'公司名称')
    title = models.CharField(max_length=15, verbose_name=u'职位')
    salary = models.CharField(max_length=15, verbose_name=u'薪资')
    quitReason = models.CharField(max_length=20, verbose_name=u'离职原因')
    witness = models.CharField(max_length=20, verbose_name=u'证明人')
    witnessPhone = models.CharField(max_length=11, verbose_name=u'证明人电话')

    class Meta:
        verbose_name = u'工作经历'
        verbose_name_plural = verbose_name


class Training(models.Model):
    startTime = models.DateTimeField(verbose_name=u'开始时间', default=datetime.now)
    endTime = models.DateTimeField(verbose_name=u'结束时间', default=datetime.now)
    trainingInstituteName = models.CharField(max_length=30, verbose_name=u'机构名称')
    trainingCourse = models.CharField(max_length=30, verbose_name=u'培训课程')
    certificate = models.CharField(max_length=30, verbose_name=u'证书名称')

    class Meta:
        verbose_name = u'培训经历'
        verbose_name_plural = verbose_name


class Family(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    relationship = models.CharField(max_length=10, verbose_name=u'关系')
    organization = models.CharField(max_length=20, verbose_name=u'单位')
    contactPhone = models.CharField(max_length=11, verbose_name=u'联系电话')

    class Meta:
        verbose_name = u'家庭状况'
        verbose_name_plural = verbose_name


class SkillSpeciality(models.Model):
    language = models.CharField(max_length=10, choices=(('english', u'英语'), ('mandarin', u'普通话'),
                                                        ('cantonese', u'粤语')), verbose_name=u'语言')
    computer = models.CharField(max_length=11, verbose_name=u'计算机')

    class Meta:
        verbose_name = u'技能特长'
        verbose_name_plural = verbose_name


class JobSource(models.Model):
    internet = models.CharField(max_length=11, verbose_name=u'互联网')
    staffIntroduce = models.CharField(max_length=11, verbose_name=u'员工介绍')

    class Meta:
        verbose_name = u'招聘途径'
        verbose_name_plural = verbose_name


class Signature(models.Model):
    signatureId = models.CharField(max_length=20, verbose_name=u'签名验证码')
    signatureDate = models.DateTimeField(verbose_name=u'签字时间', default=datetime.now)

    class Meta:
        verbose_name = u'签名'
        verbose_name_plural = verbose_name
