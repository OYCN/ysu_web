# coding:utf-8
from django.utils.deprecation import MiddlewareMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse #拼接网址
from django.conf import settings

import re

class CheckPermission(MiddlewareMixin):
    #1发送请求
    def process_request(self, request):

        # 当前访问路径
        current_path = request.path_info

        # 检查是否属于白名单
        for valid_url in settings.PERMISSION_WHITE_LIST:
            ret = re.match("^%s$" % valid_url, current_path)
            if ret:
                return None
        # 校验权限
        if request.method == 'GET':
            permission_list = request.session.get("permissions_GET",[])
        else:
            permission_list = request.session.get("permissions_POST", [])

        flag = False
        for permission in permission_list:
            permission = "^%s$" % permission
            ret = re.match(permission, current_path)
            if ret:
                flag = True
                break
        if not flag:
            raise Http404
        return request

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

