#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/15 23:18 
# @Author : Andrew
# @Site :  
# @File : autocomplete.py 
# @Software: PyCharm

from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs