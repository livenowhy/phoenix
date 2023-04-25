#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
"""

import uuid
from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField


def gen_uuid():
    return uuid.uuid4().hex


class AbstractBase(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    uuid = models.CharField(max_length=36, default=gen_uuid, unique=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True, help_text='创建时间')
    updated_at = models.DateTimeField("更新时间", auto_now_add=True, help_text='更新时间', null=True)
    deleted_at = models.DateTimeField("删除时间", help_text='删除时间', null=True)
    deleted = models.BooleanField("是否删除", default=False)
    description = models.CharField("描述信息", max_length=256, null=True, blank=True)

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                value = [i.id for i in value ] if self.pk else None
            if isinstance(f, DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data

    class Meta:
        abstract = True


class AbstractSimpleBase(models.Model):
    """ 简单的数据模型 """
    id = models.AutoField(primary_key=True, auto_created=True)
    uuid = models.CharField(max_length=36, default=gen_uuid, unique=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True, help_text='创建时间')
    description = models.CharField("描述信息", max_length=256, null=True, blank=True)

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                value = [i.id for i in value ] if self.pk else None
            if isinstance(f, DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data

    class Meta:
        abstract = True