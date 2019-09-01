from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect
# Register your models here.

@admin.register(Permission)
class Permission_admin(admin.ModelAdmin):
    list_editable = ( 'rule', 'method', 'type')
    list_display = ('name', 'rule','method', 'type')

@admin.register(Group)
class Group_admin(admin.ModelAdmin):
    readonly_fields = ('p_display',)
    list_display_links = ('name','mark')
    list_display = ('name','mark')

@admin.register(Permission_type)
class Permission_admin(admin.ModelAdmin):
    list_display = ('name','num')

@admin.register(WorkList)
class WorkList_admin(admin.ModelAdmin):
    readonly_fields = ('item',)
    list_editable = ('urls_name', 'type')
    list_display = ('name','urls_name','type')
    actions = ['tran_manage_list']

    def tran_manage_list(self, request, queryset):
        # 定义actions函数
        # 判断用户选择了几条数据，如果是一条以上，则报错
        data = queryset.values()
        for i in data:
            i.pop('id')
            # 将原数据复制并去掉id字段后，插入数据库，以实现复制数据功能，返回值即新数据的id（这是在model里__str__中定义的）
            r_pk = ManageList.objects.create(**i)
            # 修改数据后重定向url到新加数据页面
            queryset.delete()
        return HttpResponseRedirect('{}{}/change'.format(request.path, r_pk))
    tran_manage_list.short_description = "转移所选数据至管理列表"

@admin.register(ManageList)
class ManageList_admin(admin.ModelAdmin):
    readonly_fields = ('item',)
    list_editable = ( 'urls_name','type')
    list_display = ('name','urls_name','type')
    actions = ['tran_work_list']

    def tran_work_list(self, request, queryset):
        # 定义actions函数
        # 判断用户选择了几条数据，如果是一条以上，则报错
        data = queryset.values()
        for i in data:
            i.pop('id')
            # 将原数据复制并去掉id字段后，插入数据库，以实现复制数据功能，返回值即新数据的id（这是在model里__str__中定义的）
            r_pk = WorkList.objects.create(**i)
            # 修改数据后重定向url到新加数据页面
            queryset.delete()
        return HttpResponseRedirect('{}{}/change'.format(request.path, r_pk))
    tran_work_list.short_description = "转移所选数据至职务列表"

@admin.register(Duty)
class Duty_admin(admin.ModelAdmin):
    list_display = ('name','mark')

@admin.register(User)
class User_admin(admin.ModelAdmin):
    readonly_fields = ('p_display','w_display','m_display')
    list_display = ('name', 'major', 'department', 'has_pmixin', 'has_wmixin', 'has_mmixin')
