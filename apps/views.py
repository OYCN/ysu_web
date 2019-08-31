from django.shortcuts import render
from ysu_web.settings import STATIC_URL

# Create your views here.
def all_apps(request):
    index_type = 'apps'
    app_list = [
        {
            'name':'测试应用',
            'img':STATIC_URL + 'img/bili.jpg',
            'url':'#',
        },
    ]
    return render(request, 'apps/apps.html', locals())