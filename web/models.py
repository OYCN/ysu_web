from django.db import models
from .data import *
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html

from multiselectfield import MultiSelectField
from ckeditor_uploader.fields import RichTextUploadingField

from django.conf import settings

from itertools import chain

# python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata model_init.json
# python manage.py dumpdata

# Create your models here.
class Allow_num(models.Model):
    #注册码结构:id(16进制)+'G'+code
    class Meta:
        verbose_name = '注册码'
        verbose_name_plural = '注册码'
    #注册码权限等级
    duty = models.ForeignKey('web_permission.Duty', on_delete=models.CASCADE, null=False, blank=False, verbose_name=u'注册职务')
    #注册码主体
    code = models.CharField(max_length=10, null=False, blank=False,verbose_name="码值")

    def __str__(self):
        return self.code
    def full_code(self):
        return (str(hex(int(self.id)))+'Z'+str(self.code))
    full_code.short_description = "完整注册码"

# class User(models.Model):
#     class Meta:
#         verbose_name = '社团成员'
#         verbose_name_plural = '社团成员'
#     #姓名
#     name = models.CharField(max_length=5,verbose_name="姓名")
#     #ID卡号
#     idcard = models.CharField(max_length=12,unique=True,verbose_name="ID卡号")
#     #职务
#     duty = models.ForeignKey('web_permission.Duty', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'职务')
#     #学院
#     college = models.CharField(choices=college_list,max_length=2,verbose_name="学院")
#     #专业
#     major = models.CharField(choices=major_list,max_length=2,verbose_name="专业")
#     #部门
#     department = models.CharField(max_length=50,verbose_name="部门")
#     #方向
#     direction = models.CharField(max_length=50,verbose_name="方向")
#     #邮箱
#     email = models.EmailField(max_length=50,verbose_name="邮箱")
#     #地址
#     address = models.CharField(max_length=50,verbose_name="地址")
#     #密码 make_password("") 为78个字符
#     passwd = models.CharField(max_length=80,verbose_name="密码")
#     #权限
#     # authority = MultiSelectField(choices=authority_list,null=True,blank=True,verbose_name="权限")
#     group = models.ManyToManyField('web_permission.Group', null=True, blank=True, verbose_name=u'地址访问权限组')
#     pmixin = models.ManyToManyField('web_permission.Permission', null=True, blank=True, verbose_name=u'额外地址访问权限')
#     #额外职务列表
#     wmixin = models.ManyToManyField('web_permission.WorkList', null=True, blank=True, verbose_name=u'额外职务列表')
#     #额外管理列表
#     mmixin = models.ManyToManyField('web_permission.ManageList', null=True, blank=True, verbose_name=u'额外管理列表')
#
#     #用户组列表
#     def group_marks(self):
#         l = set()
#         for i in self.group.all():
#             l.add(i.mark)
#         return list(l)
#     #权限列表
#     def permissions(self):
#         l=set()
#         ll = {'GET':set(),'POST':set(),'PG':set()}
#         for i in self.group.all():
#             for j in i.permission.all():
#                 l.add(j)
#         for i in self.pmixin.all():
#             l.add(i)
#         for i in l:
#             ll[i.method].add((i.rule))
#         ll['GET'].update(ll['PG'])
#         ll['POST'].update(ll['PG'])
#         return (list(['GET']), list(ll['POST']))
#     def p_display(self):
#         l = set()
#         for i in self.group.all():
#             for j in i.permission.all():
#                 l.add(j)
#         for i in self.pmixin.all():
#             l.add(i)
#         return format_html('<br>'.join([i.p_display() for i in l]))
#     p_display.short_description = u'所有地址访问权限'
#     #职务列表
#     def work_list(self):
#         l = set()
#         for i in self.group.all():
#             for j in i.work_list.all():
#                 l.add(j.item())
#         for i in self.wmixin.all():
#             l.add(i.item())
#         return list(l)
#     def w_display(self):
#         l = set()
#         for i in self.group.all():
#             for j in i.work_list.all():
#                 l.add(j)
#         for i in self.wmixin.all():
#             l.add(i)
#         return format_html('<br>'.join([i.p_display() for i in l]))
#     w_display.short_description = u'所有职务内容'
#     #管理列表
#     def manage_list(self):
#         l  = set()
#         for i in self.group.all():
#             for j in i.manage_list.all():
#                 l.add(j.item())
#         for i in self.mmixin.all():
#             l.add(i.item())
#         return list(l)
#     def m_display(self):
#         l = set()
#         for i in self.group.all():
#             for j in i.manage_list.all():
#                 l.add(j)
#         for i in self.mmixin.all():
#             l.add(i)
#         return format_html('<br>'.join([i.p_display() for i in l]))
#     m_display.short_description = u'所有管理内容'
#
#     def has_pmixin(self):
#         if self.pmixin.count() == 0:
#             self.color = 'green'
#             self.isit = '有'
#         else:
#             self.color = 'red'
#             self.isit = '无'
#         return format_html(
#             '<span style="color: #{};"></span>',
#             self.color,
#             self.isit,
#         )
#     has_pmixin.short_description = u'附加地址访问权限'
#
#     def has_wmixin(self):
#         if self.wmixin.count() == 0:
#             self.color = 'green'
#             self.isit = '有'
#         else:
#             self.color = 'red'
#             self.isit = '无'
#         return format_html(
#             '<span style="color: #{};"></span>',
#             self.color,
#             self.isit,
#         )
#     has_wmixin.short_description = u'附加职务内容'
#
#     def has_mmixin(self):
#         if self.pmixin.count() == 0:
#             self.color = 'green'
#             self.isit = '有'
#         else:
#             self.color = 'red'
#             self.isit = '无'
#         return format_html(
#             '<span style="color: #{};"></span>',
#             self.color,
#             self.isit,
#         )
#     has_mmixin.short_description = u'附加管理内容'
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if self.pk is None:
#             flag = True
#         else:
#             flag = False
#         super().save(*args, **kwargs)  # Call the "real" save() method.
#         if flag:
#             self.group.set(self.duty.default_group.all())
#             self.pmixin.set(self.duty.default_pmixin.all())
#             self.wmixin.set(self.duty.default_work_list.all())
#             self.mmixin.set(self.duty.default_manage_list.all())

class NewUser(models.Model):
    class Meta:
        verbose_name = '萌新'
        verbose_name_plural = '萌新'
    # 姓名
    name = models.CharField(max_length=5, verbose_name="姓名")
    # 手机号
    tel = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    # 学院
    college = models.CharField(choices=college_list, max_length=2, verbose_name="学院")
    # 专业
    major = models.CharField(choices=major_list, max_length=2, verbose_name="专业")
    # 方向
    direction = models.CharField(max_length=10, verbose_name="方向")
    # 是否同意调剂
    accept = models.CharField(max_length=10, verbose_name="调剂",blank=True,null=True)
    # 留言
    message = models.CharField(max_length=160, verbose_name="留言")


@python_2_unicode_compatible
class Article(models.Model):
    class Meta:
        verbose_name = '消息通知'
        verbose_name_plural = '消息通知'
    title = models.CharField(max_length=50,unique=True,verbose_name=u"标题")
    idcard = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,verbose_name=u"作者ID")
    brief = models.TextField(null=True, blank=True,verbose_name=u"简述")
    image = models.TextField(null=True, blank=True,verbose_name=u"配图")
    content = RichTextUploadingField(verbose_name=u"内容")
    create = models.DateTimeField(auto_now_add=True,verbose_name=u"创建日期")
    latest = models.DateTimeField(auto_now=True,verbose_name=u"修改日期")

    def __str__(self):
        return self.title
    def author(self):
        return self.idcard.name
    author.short_description = "作者"

class Counter(models.Model):
    class Meta:
        verbose_name = '计数器'
        verbose_name_plural = '计数器'
    counter = models.IntegerField()
    name = models.CharField(max_length=10, verbose_name="功能", unique=True, default=0)

    @staticmethod
    def add(name,num=1):
        adder = Counter.objects.filter(name=name)
        if len(adder) == 1:
            adder.counter = adder.counter + num
            adder.save()
            return True
        else:
            return False

    @staticmethod
    def safe_add(name, num=1):
        adder = Counter.objects.filter(name=name)
        if len(adder) == 1:
            counter = adder[0].counter + num
            adder[0].counter = counter
            adder[0].save()
            return counter
        elif len(adder) == 0:
            Counter.objects.create(name=name, counter=1)
            return 1
        else:
            return False

    @staticmethod
    def create(name):
        if not Counter.objects.filter(name=name):
            Counter.objects.create(name=name,counter=0)
            return True
        else:
            return False