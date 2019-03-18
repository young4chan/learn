#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

if __name__=='__main__':
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('test pass')
    else:
        print('test fail')

