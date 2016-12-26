#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-

# break 跳出循环是指跳出离自己最近的循环
for n in range(2,10):
    for i in range(2,n):
        if n % i == 0:
            print (n,'equals',i,'*',n//i )
            break
    else:
            print (n,'is a prime number')
