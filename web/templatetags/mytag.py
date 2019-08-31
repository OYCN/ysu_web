# coding:utf-8
from django import template
register = template.Library()

#只能加一个变量
#   {{xxx|xxx:x}}
@register.filter
def search_title(title, key):
    for i in key:
        title = title.replace(i,'<span class="text-warning">'+i+'</span>')
    return title

@register.filter
def indx(title, i):
    return title[int(i)]

@register.filter
def keyis(title, i):
    return title[i]

#多个变量
#{% funx x x x x&}
# @register.simple_tag