#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender.lower() in ['male', 'female']:
            self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('test fail 1 ')
else:
    print('test pass 1 ')

bart.set_gender('Female')

if bart.get_gender() != 'Female':
    print('test fail 2 ')
else:
    print('test pass 2 ')
