#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import getpass

user = input("username:")
pwd = getpass.getpass("password:")
if user == "root" and pwd == "123":
    print ("Login sucess")
else:
    print ("Login failure")