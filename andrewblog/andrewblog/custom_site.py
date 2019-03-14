#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/13 22:29 
# @Author : Andrew
# @Site :  
# @File : custom_site.py 
# @Software: PyCharm

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'andrew_blog后台管理'
    site_title = 'andrew_blog管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')