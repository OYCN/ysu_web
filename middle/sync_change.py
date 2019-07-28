# coding:utf-8
from django.utils.deprecation import MiddlewareMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse #拼接网址
from django.conf import settings
from web.models import *

import re

class SyncChange(MiddlewareMixin):
    #1发送请求
    def process_request(self, request):
        if request.session.get('islogin',False):
            u = User.objects.get(idcard=request.session['idcard'])
            if u:
                if request.session['idcard'] in settings.USER_NEED_SYNC_SESSION:
                    request.session['name'] = u.name
                    request.session['duty'] = u.duty.name
                    request.session['permissions_GET'], request.session['permissions_POST'] = u.permissions()
                    request.session['group_marks'] = u.group_marks()
                    request.session['work_list'] = u.work_list()
                    request.session['manage_list'] = u.manage_list()
                    settings.USER_NEED_SYNC_SESSION.discard(request.session['idcard'])
            else:
                request.session['islogin'] = False
        return None

    #2执行完 request 预处理函数并确定待执行的 view 之后，但在 view 函数实际执行之前。
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     pass

    #4收集错误信息
    # def process_exception(self, request, exception):
    #     pass

    #5必须返回 HttpResponse 对象. 这个 response 对象可以是传入函数的那一个原始对象（通常已被修改），也可以是全新生成的。
    # def process_response(self, request, response):
    #     return response
    #3
    # def process_template_response(self, request, response):
    #     pass