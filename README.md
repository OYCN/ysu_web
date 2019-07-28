# ysu_web
基于django为学校社团创建的网站

安装环境：

```
pip install -r requirements.txt
```

迁移数据库：

```
python manage.py makemigrations
python manage.py migrate
```

加载示例数据：

```
python manage.py loaddata model_init.json
```

创建超级管理员：

```
python ./manage.py createsuperuser
```

开发运行：

```
python manage.py runserver [ip:port]
```

搜集静态文件：

```
python ./manage.py collectstatic
```

上线运行（需配置服务器）：

```
uwsgi --http ip:port --chdir /path/to/project --home=/path/to/env --module project.wsgi
```

