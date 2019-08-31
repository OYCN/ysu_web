from django.contrib import admin
from .models import *
from .logic import gen_code
from django.conf import settings
# Register your models here.

admin.site.site_header = '后台底层管理'
admin.site.site_title = '后台底层管理'

@admin.register(Allow_num)
class Allow_num_admin(admin.ModelAdmin):
    exclude = ['code']
    list_display = ('id', 'duty', 'code', 'full_code')
    list_display_links = ('id', 'code')

    def save_model(self, request, obj, form, change):
        obj.code = gen_code()
        super(Allow_num_admin, self).save_model(request, obj, form, change)

@admin.register(User)
class User_admin(admin.ModelAdmin):
    readonly_fields = ('p_display','w_display','m_display')
    list_display = ('name', 'major', 'department', 'has_pmixin', 'has_wmixin', 'has_mmixin')

@admin.register(Article)
class Article_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create','latest')

@admin.register(NewUser)
class NewUser_admin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'college','major', 'direction')

@admin.register(Counter)
class Counter_admin(admin.ModelAdmin):
    readonly_fields = ('name', 'counter')
    list_display = ('name', 'counter')