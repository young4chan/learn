#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if __name__ == '__main__':
    bart = Student('Bart')
    print(Student.count)
    lisa = Student('Lisa')
    print(Student.count)

