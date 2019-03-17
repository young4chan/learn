#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must be positive!')
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must be positive!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

if __name__=='__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)


