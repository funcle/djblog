#!/usr/bin/python
# -*- utf-8 -*-

import datetime
from django import template

register = template.Library()

def time_to_format(value):
    from essay.choices import MONTHDICT
    if not isinstance(value, datetime.datetime):
    	return value
    year, month, day = value.year, value.month, value.day
    month_str = MONTHDICT.get(month)
    return "".join([month_str, " ", str(day), ", ",str(year)])
register.filter('time_to_format', time_to_format)


def ym_to_china(value):
    year, month = value.split("-")
    return "-".join([year, month])
register.filter('ym_to_china', ym_to_china)


def to_timestamp(value):
    return value.strftime('%Y-%m-%d %H:%M:%S') if value else value
register.filter('to_timestamp', to_timestamp)


def content_length_control(value):
    rs = value[0:650]+"..." if len(value)> 650 else value
    print rs
    return value[0:650]+"..." if len(value)> 650 else value
register.filter('content_length_control', content_length_control)
