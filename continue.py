#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-

# continue 条件不满足，略过此次代码，循环继续往下执行
for num in range(2,10):
    if num % 2 ==0:
        print ("Found an even number", num)
        continue
    print ("Found a number", num)