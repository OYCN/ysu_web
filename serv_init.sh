#!/usr/bin/env bash
#sed -i 's/\r$//' filename

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py loaddata model_init.json

#python ./manage.py createsuperuser

#python ./manage.py collectstatic

# 请在 ckeditor_uploader/urls.py 里将 staff_member_required 修饰器删除， 防止无法上传文件

