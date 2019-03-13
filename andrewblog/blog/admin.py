# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 列表页面显示的字段
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')
    # 添加页面显示的字段
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        # request.user当前登录的用户名，如果没有登录就是匿名用户
        obj.owner = request.user
        # obj是当前要保存的对象， form提交过来的表单之后的对象，change标志是新增还是更新
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        # request.user当前登录的用户名，如果没有登录就是匿名用户
        obj.owner = request.user
        # obj是当前要保存的对象， form提交过来的表单之后的对象，change标志是新增还是更新
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_time', 'operator']
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category_name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    fields = ('category', 'title', 'desc', 'status', 'content', 'tag')

    def operator(self, obj):
        # reverse根据名称解析URL地址
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        # request.user当前登录的用户名，如果没有登录就是匿名用户
        obj.owner = request.user
        # obj是当前要保存的对象， form提交过来的表单之后的对象，change标志是新增还是更新
        return super(PostAdmin, self).save_model(request, obj, form, change)

