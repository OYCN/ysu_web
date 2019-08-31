from django.db import models
from django.utils.html import format_html
from django.urls import reverse #拼接网址
import django

# python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata model_init.json

# Create your models here.
class Permission(models.Model):
    method_list = (
        ('GET','GET'),
        ('POST','POST'),
        ('PG','POST&GET')
    )
    class Meta:
        verbose_name = '所有地址访问权限'
        verbose_name_plural = '所有地址访问权限'
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=u'权限名')
    rule = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name=u'允许的url正则')
    method = models.CharField(choices=method_list,max_length=4, null=False, blank=False, verbose_name=u'允许方法')
    type = models.ForeignKey('web_permission.Permission_type', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u"所属类型")
    def p_display(self):
        if self.type:
            return self.type.name + '||' + self.name
        else:
            return '---||' + self.name
    p_display.short_description = u'所有地址访问权限'

    def __str__(self):
        return self.name

class Permission_type(models.Model):
    class Meta:
        verbose_name = '地址访问权限类别'
        verbose_name_plural = '地址访问权限类别'
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=u'权限类别')

    def num(self):
        return self.permission_set.count()
    num.short_description = u'地址访问权限个数'

    def __str__(self):
        return self.name

class Group(models.Model):
    class Meta:
        verbose_name = '地址访问权限组'
        verbose_name_plural = '地址访问权限组'
    name = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name=u'组名')
    mark = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name=u'代码')
    permission = models.ManyToManyField('web_permission.Permission', null=True, blank=True, verbose_name=u'拥有权限')
    work_list = models.ManyToManyField('web_permission.WorkList', null=True, blank=True, verbose_name=u'职务列表')
    manage_list = models.ManyToManyField('web_permission.ManageList', null=True, blank=True, verbose_name=u'管理列表')

    def p_display(self):
        l = set()
        for i in self.permission.all():
            l.add(i.p_display())
        return format_html('<br>'.join(list(l)))
    p_display.short_description = u'所有地址访问权限'

    def __str__(self):
        return self.name

class WorkList(models.Model):
    class Meta:
        verbose_name = '职务列表'
        verbose_name_plural = '职务列表'
    name = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=u'职务名称')
    urls_name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=u'urls中的name')
    type = models.ForeignKey('web_permission.Permission_type', on_delete=models.SET_NULL, null=True, verbose_name=u"归属权限类型")

    def item(self):
        try:
            return (self.name, reverse(self.urls_name))
        except django.urls.exceptions.NoReverseMatch:
            return (self.name, "#无匹配url")
    item.short_description = u'职务信息元组'

    def __str__(self):
        return self.name

class ManageList(models.Model):
    class Meta:
        verbose_name = '管理列表'
        verbose_name_plural = '管理列表'
    name = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name=u'管理名称')
    urls_name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=u'urls中的name')
    type = models.ForeignKey('web_permission.Permission_type', on_delete=models.SET_NULL, null=True, verbose_name=u"归属权限类型")

    def item(self):
        try:
            return (self.name, reverse(self.urls_name))
        except django.urls.exceptions.NoReverseMatch:
            return (self.name, "#无匹配url")
    item.short_description = u'管理信息元组'

    def __str__(self):
        return self.name

class Duty(models.Model):
    class Meta:
        verbose_name = '社团所属职务'
        verbose_name_plural = '社团所属职务'
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=u'职务名称')
    mark = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name=u'职务代码')
    default_group = models.ManyToManyField('web_permission.Group', null=True, blank=True, verbose_name=u'初始归属用户组')
    default_pmixin = models.ManyToManyField('web_permission.Permission', null=True, blank=True, verbose_name=u'初始组外权限')
    default_work_list = models.ManyToManyField('web_permission.WorkList', null=True, blank=True, verbose_name=u'初始职务列表')
    default_manage_list = models.ManyToManyField('web_permission.ManageList', null=True, blank=True, verbose_name=u'初始管理列表')

    def __str__(self):
        return self.name