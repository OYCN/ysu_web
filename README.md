# ysu_web

> 基于django为学校社团创建的网站

### 必要告知：

- 本网站为**个人**制作，不代表**集体**
- 网站中**全部信息**为网站**测试**使用，**不是**真实信息
- 源码处于**开发**阶段，**不提供**技术支持

### 源码使用须知：

- `ysu_web/settings.py`文件需要用户自行配置并添加 `SECRET_KEY`
- 源码上线前需将 `DEBUG`设置为`False`
- 请将环境中的包 `ckeditor_uploader/urls.py` 里将 `staff_member_required` 函数(修饰器)删除， 防止未登入后台无法上传文件
- 剩余后续补充

### 基本操作：

**安装环境：**

```
pip install -r requirements.txt
```

**迁移数据库：**

```
python manage.py makemigrations
python manage.py migrate
```

**加载示例数据：**

```
python manage.py loaddata model_init.json
```

**创建超级管理员：**

```
python ./manage.py createsuperuser
```

**开发运行：**

```
python manage.py runserver [ip:port]
```

**搜集静态文件：**

```
python ./manage.py collectstatic
```

**上线运行（需配置服务器）：**

```
uwsgi --http ip:port --chdir /path/to/project --home=/path/to/env --module project.wsgi
```
