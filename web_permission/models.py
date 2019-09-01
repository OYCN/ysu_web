from django.db import models
from django.utils.html import format_html
from django.urls import reverse #拼接网址
import django

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

from web.data import *

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


# models.py
from django.contrib.auth.base_user import BaseUserManager


# 重写UserManager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, idcard, password, **extra_fields):
        if not idcard:
            raise ValueError("请填入idcard！")
        if not password:
            raise ValueError("请填入密码!")
        user = self.model(idcard=idcard, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, idcard, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(idcard, password, **extra_fields)

    def create_superuser(self, idcard, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(idcard, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    class Meta:
        verbose_name = '社团成员'
        verbose_name_plural = '社团成员'

    # 是否管理员
    is_staff = models.BooleanField(default=False)
    # 是否可用
    is_active = models.BooleanField(default=True)

    #姓名
    name = models.CharField(max_length=10,verbose_name="姓名")
    #ID卡号
    idcard = models.CharField(max_length=12,unique=True,verbose_name="ID卡号")
    #职务
    duty = models.ForeignKey('web_permission.Duty', on_delete=models.SET_NULL, verbose_name=u'职务', null=True, blank=True)
    #学院
    college = models.CharField(choices=college_list,max_length=2,verbose_name="学院", null=True, blank=True)
    #专业
    major = models.CharField(choices=major_list,max_length=2,verbose_name="专业", null=True, blank=True)
    #部门
    department = models.CharField(max_length=50,verbose_name="部门", null=True, blank=True)
    #方向
    direction = models.CharField(max_length=50,verbose_name="方向", null=True, blank=True)
    #邮箱
    email = models.EmailField(max_length=50,verbose_name="邮箱", null=True, blank=True)
    #地址
    address = models.CharField(max_length=50,verbose_name="地址", null=True, blank=True)
    # #密码 make_password("") 为78个字符
    # passwd = models.CharField(max_length=80,verbose_name="密码")
    #权限
    # authority = MultiSelectField(choices=authority_list,null=True,blank=True,verbose_name="权限")
    group = models.ManyToManyField('web_permission.Group', null=True, blank=True, verbose_name=u'地址访问权限组')
    pmixin = models.ManyToManyField('web_permission.Permission', null=True, blank=True, verbose_name=u'额外地址访问权限')
    #额外职务列表
    wmixin = models.ManyToManyField('web_permission.WorkList', null=True, blank=True, verbose_name=u'额外职务列表')
    #额外管理列表
    mmixin = models.ManyToManyField('web_permission.ManageList', null=True, blank=True, verbose_name=u'额外管理列表')

    USERNAME_FIELD = 'idcard'
    REQUIRED_FIELDS = ['name',]

    # 重定义 manager
    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    #用户组列表
    def group_marks(self):
        l = set()
        for i in self.group.all():
            l.add(i.mark)
        return list(l)
    #权限列表
    def permissions(self):
        l=set()
        ll = {'GET':set(),'POST':set(),'PG':set()}
        for i in self.group.all():
            for j in i.permission.all():
                l.add(j)
        for i in self.pmixin.all():
            l.add(i)
        for i in l:
            ll[i.method].add((i.rule))
        ll['GET'].update(ll['PG'])
        ll['POST'].update(ll['PG'])
        return (list(['GET']), list(ll['POST']))
    def p_display(self):
        l = set()
        for i in self.group.all():
            for j in i.permission.all():
                l.add(j)
        for i in self.pmixin.all():
            l.add(i)
        return format_html('<br>'.join([i.p_display() for i in l]))
    p_display.short_description = u'所有地址访问权限'
    #职务列表
    def work_list(self):
        l = set()
        for i in self.group.all():
            for j in i.work_list.all():
                l.add(j.item())
        for i in self.wmixin.all():
            l.add(i.item())
        return list(l)
    def w_display(self):
        l = set()
        for i in self.group.all():
            for j in i.work_list.all():
                l.add(j)
        for i in self.wmixin.all():
            l.add(i)
        return format_html('<br>'.join([i.p_display() for i in l]))
    w_display.short_description = u'所有职务内容'
    #管理列表
    def manage_list(self):
        l  = set()
        for i in self.group.all():
            for j in i.manage_list.all():
                l.add(j.item())
        for i in self.mmixin.all():
            l.add(i.item())
        return list(l)
    def m_display(self):
        l = set()
        for i in self.group.all():
            for j in i.manage_list.all():
                l.add(j)
        for i in self.mmixin.all():
            l.add(i)
        return format_html('<br>'.join([i.p_display() for i in l]))
    m_display.short_description = u'所有管理内容'

    def has_pmixin(self):
        if self.pmixin.count() == 0:
            self.color = 'green'
            self.isit = '有'
        else:
            self.color = 'red'
            self.isit = '无'
        return format_html(
            '<span style="color: #{};"></span>',
            self.color,
            self.isit,
        )
    has_pmixin.short_description = u'附加地址访问权限'

    def has_wmixin(self):
        if self.wmixin.count() == 0:
            self.color = 'green'
            self.isit = '有'
        else:
            self.color = 'red'
            self.isit = '无'
        return format_html(
            '<span style="color: #{};"></span>',
            self.color,
            self.isit,
        )
    has_wmixin.short_description = u'附加职务内容'

    def has_mmixin(self):
        if self.pmixin.count() == 0:
            self.color = 'green'
            self.isit = '有'
        else:
            self.color = 'red'
            self.isit = '无'
        return format_html(
            '<span style="color: #{};"></span>',
            self.color,
            self.isit,
        )
    has_mmixin.short_description = u'附加管理内容'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            flag = True
        else:
            flag = False
        super().save(*args, **kwargs)  # Call the "real" save() method.
        if flag:
            if self.duty != None:
                self.group.set(self.duty.default_group.all())
                self.pmixin.set(self.duty.default_pmixin.all())
                self.wmixin.set(self.duty.default_work_list.all())
                self.mmixin.set(self.duty.default_manage_list.all())
