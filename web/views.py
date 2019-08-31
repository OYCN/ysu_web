# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse #文本方式返回
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse #拼接网址
from django.contrib.auth.hashers import make_password, check_password

from .forms import *
from .models import *

import re

# Create your views here.
def welcome(request):
    return render(request, 'web/welcome.html', locals())

def index(request):
    index_type = 'index'
    return render(request, 'web/index.html', locals())

def info(request):
    index_type = 'info'
    a = Article.objects.all()[:5]
    return render(request, 'web/info.html', locals())

def newuser(request):
    data_college = college_list
    data_major = major_select_list
    return render(request, 'web/newuser.html', locals())

def login(request):
    is_relogin = False
    info = ''
    color = 'danger'
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            u = User.objects.filter(idcard=form.cleaned_data['idcard'])
            if u:
                if check_password(form.cleaned_data['passwd'], u[0].passwd):
                    request.session['islogin'] = True
                    request.session['idcard'] = u[0].idcard
                    request.session['name'] = u[0].name
                    request.session['duty'] = u[0].duty.name
                    request.session['permissions_GET'], request.session['permissions_POST'] = u[0].permissions()
                    request.session['group_marks'] = u[0].group_marks()
                    request.session['work_list'] = u[0].work_list()
                    request.session['manage_list'] = u[0].manage_list()
                    if form.cleaned_data.get('rem','0') != '1':
                        request.session.set_expiry(0)
                    return HttpResponseRedirect(reverse('index'))
        info = '用户名或密码错误'
        color = 'danger'
        is_relogin = True
        return render(request, 'web/login.html', locals())
    else:
        if request.session.get('islogin',False):
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'web/login.html', locals())

def logout(request):
    if request.session.get('islogin', False):
        request.session.flush()
    return HttpResponseRedirect(reverse('index'))

def register(request):
    is_reregister = False
    data_college = college_list
    data_major = major_select_list
    data_duty = [[i.mark, i.name] for i in Duty.objects.all()]
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            if not User.objects.filter(idcard=form.cleaned_data['idcard']):
                t = form.cleaned_data['allow_num'].split('Z')
                if len(t) == 2:
                    id, code = t
                    try:
                        id = str(int(id,16))
                    except ValueError:
                        is_reregister = True
                        info = '注册码无效'
                        return render(request, 'web/register.html', locals())
                    c = Allow_num.objects.filter(id=id)
                    if c:
                        if c[0].code == code and c[0].duty.mark == form.cleaned_data['duty']:
                            User.objects.create(
                                name=form.cleaned_data['name'],
                                idcard=form.cleaned_data['idcard'],
                                duty=Duty.objects.get(mark=form.cleaned_data['duty']),
                                college=form.cleaned_data['college'],
                                major=form.cleaned_data['major'],
                                department=form.cleaned_data['department'],
                                direction=form.cleaned_data['direction'],
                                email=form.cleaned_data['email'],
                                address=form.cleaned_data['address'],
                                passwd=make_password(form.cleaned_data['passwd']),
                            )
                            c[0].delete()
                            is_relogin = True
                            info = '可以登陆了'
                            color = 'success'
                            return render(request, 'web/login.html',locals())
                is_reregister = True
                info = '注册码无效'
                return render(request, 'web/register.html', locals())
            else:
                is_reregister = True
                info = '此ID卡号已被注册'
                return render(request, 'web/register.html', locals())
        else:
            is_reregister = True
            if len(form.cleaned_data['idcard'])!=12:
                info = 'ID卡号不合法'
            else:
                info = '表单不合法'
                print(form.errors)
            return render(request, 'web/register.html', locals())
    else:
        return render(request, 'web/register.html', locals())

def search(request):
    string = re.split(r'[!"#\$%&\'\(\)\*\+,-./:;<=>\?@\[\\\]\^_`\{\|\}~ ，。、；：‘’“”…]', request.GET.get('search', ''))
    string = [i for i in string if i != '']
    if len(string)!=0:
        result = Article.objects.filter(title__icontains=string[0])
        if len(string)>1:
            for i in string[1:]:
                result = result.filter(title__icontains=i)
    else:
        result = None
    return render(request, 'web/search.html', locals())

def article(request, id):
    a = Article.objects.get(id=id)
    return render(request, 'web/article.html', locals())

def publish(request):
    form = Publish_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            a = Article()
            a.title = form.cleaned_data['title']
            a.idcard = User.objects.get(idcard = request.session['idcard'])
            a.brief = request.POST.get('brief','')
            a.image = request.POST.get('image','')
            a.content = form.cleaned_data['content']
            a.save()
            return HttpResponseRedirect(reverse('info'))
        return HttpResponse(form.errors)
    else:
        return render(request, 'manage/publish.html', locals())
