#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
"""

from django.db import models

from .base import AbstractBase

from common.constant.transfer_info import BankType, TransferType


class TransferInfoModel(AbstractBase):
    """
    转账流水
    """
    bank = models.CharField('银行', max_length=8, choices=BankType().fetch_choices(), default='pingan')
    counterparty_name = models.CharField('交易方姓名', max_length=126)
    counterparty_account = models.CharField('交易方账号', max_length=126)

    transfer_type = models.CharField('交易类型', max_length=8, choices=TransferType().fetch_choices(), default='out')      #  转出/转入
    transfer_amount = models.DecimalField('交易金额', max_digits=8, decimal_places=2)
    transfer_time = models.DateTimeField("交易时间", help_text='交易时间', null=True)
    account_balances = models.DecimalField('账户余额', max_digits=8, decimal_places=2)
    abstract = models.CharField('摘要', max_length=32)
    serial_number = models.CharField('交易流水号', max_length=32)

    @property
    def unique_together(self):
        return ('bank', 'serial_number')  # 确定唯一

    # 备注
    class Meta:
        managed = True
        db_table = 'transfer_info'
        verbose_name = u'转账流水'
        verbose_name_plural = u'转账流水'
        unique_together = ('bank', 'serial_number')  # 确定唯一
