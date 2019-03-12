# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 列表页面显示的字段
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    # 添加页面显示的字段
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        # request.user当前登录的用户名，如果没有登录就是匿名用户
        obj.owner = request.user
        # obj是当前要保存的对象， form提交过来的表单之后的对象，change标志是新增还是更新
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        # request.user当前登录的用户名，如果没有登录就是匿名用户
        obj.owner = request.user
        # obj是当前要保存的对象， form提交过来的表单之后的对象，change标志是新增还是更新
        return super(TagAdmin, self).save_model(request, obj, form, change)