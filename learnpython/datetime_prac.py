#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
     cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
     tz = re.match(r'^UTC([\+\-0-9]*)\:\d*$', tz_str)
     if tz:
         n = tz.group(1)
     tz_utc = timezone(timedelta(hours=int(n)))
     dt = cday.replace(tzinfo=tz_utc)
     return  dt.timestamp()

if __name__ == '__main__':
    print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))
    print(to_timestamp('2015-5-31 16:10:30', 'UTC-9:00'))

