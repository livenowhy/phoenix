#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@data: 2022/11/14
"""


from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'demo'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--all', type=bool, default=False, help='全部实例')
        parser.add_argument('-func', '--func', type=str, help='执行那个函数')

    def demo(self, *args, **options):
        """
        python3 manage.py demo -func=demo
        """
        print('demo commands')

    def handle(self, *args, **options):
        func = options.get('func')
        fun = getattr(self, func)
        fun(*args, **options)
        print('options 参数: %s' % (options))