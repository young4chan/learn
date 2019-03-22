#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

msg = Parser().parsestr(msg_content)

def print_info(msg, indent=0):
    if indent == 0:
