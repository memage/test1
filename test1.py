#!/usr/bin/env python3
# coding=utf-8

a = int(input('Введите А: '))
b = int(input('Введите B: '))
x = int(input('Введите X: '))
if x >= 8:
    y =  ((a ** 2) + (4 * x ** 2) + (b ** 2)) / a * b
else:
    y = x * (a - b)

print("y = %.1f" % y)
