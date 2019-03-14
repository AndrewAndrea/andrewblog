#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/13 22:45 
# @Author : Andrew
# @Site :  
# @File : adminforms.py 
# @Software: PyCharm

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea,
                           label='摘要', required=False)