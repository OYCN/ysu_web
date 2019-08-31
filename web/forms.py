# coding:utf-8

from django import forms
from django.core import validators

from ckeditor_uploader.fields import RichTextUploadingFormField

from .data import *
from .models import *
from web_permission.models import *

class Search_form(forms.Form):
    find = forms.CharField(max_length=5)

class Login_form(forms.Form):
    idcard_rule = validators.RegexValidator(r'^[0-9]*$', '只允许数字输入')
    idcard = forms.CharField(
        required=True,
        max_length=12,
        validators=[idcard_rule]
    )
    passwd = forms.CharField(
        required=True,
        max_length=20
    )
    rem = forms.CharField(
        required=False,
        max_length=1
    )

class Register_form(forms.Form):
    idcard_rule = validators.RegexValidator(r'^[0-9]*$', '只允许数字输入')
    allow_num_rule = validators.RegexValidator(r'^0x[0-9a-fA-F]+Z[0-9a-yA-Y!#$%&*+-=?@]{10}$', '注册码不合法')
    idcard = forms.CharField(
        required=True,
        max_length=12,
        validators=[idcard_rule]
    )
    name = forms.CharField(
        required=True,
        max_length=5
    )
    duty = forms.CharField(
        required=True,
        max_length=10
    )
    college = forms.ChoiceField(
        required=True,
        choices=college_list
    )
    major = forms.ChoiceField(
        required=True,
        choices=major_list
    )
    department = forms.CharField(
        required=True,
        max_length=50
    )
    direction = forms.CharField(
        required=True,
        max_length=50
    )
    email = forms.CharField(
        required=True,
        max_length=50
    )
    address = forms.CharField(
        required=True,
        max_length=50
    )
    passwd = forms.CharField(
        required=True,
        max_length=20
    )
    allow_num = forms.CharField(
        required=True,
        # validators=[allow_num_rule]
    )

class Publish_form(forms.Form):
    title = forms.CharField(max_length=50)
    content = RichTextUploadingFormField()
