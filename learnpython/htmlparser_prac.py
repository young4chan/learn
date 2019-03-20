#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import urlopen
from contextlib import closing


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.parsedata= ''

    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            self.parsedata = 'time'
        if ('class', 'event-title') in attrs:
            self.parsedata = 'title'
        if ('class', 'event-location') in attrs:
            self.parsedata = 'location'

    def handle_data(self, data):
        if 'time' == self.parsedata:
            print('time: %s' % data)
        if 'title' == self.parsedata:
            print('event title: %s' % data)
        if 'location' == self.parsedata:
            print('location: %s' % data)
    def handle_endtag(self, tag):
        self.parsedata = ''

if __name__ == '__main__':
    parser = MyHTMLParser()
    URL = 'https://www.python.org/events/python-events/'
    with closing(urlopen(URL, timeout=15)) as page:
        for line in page:
            parser.feed(line.decode('utf-8'))
