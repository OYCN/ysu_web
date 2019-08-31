#!/usr/bin/env bash
#sed -i 's/\r$//' filename

python3 ./manage.py makemigrations
python3 ./manage.py migrate
python3 ./manage.py loaddata model_init.json

#python3 ./manage.py createsuperuser

#python3 ./manage.py collectstatic

# 请在 ckeditor_uploader/urls.py 里将 staff_member_required 修饰器删除， 防止无法上传文件

