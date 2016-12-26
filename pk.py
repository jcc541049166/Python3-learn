#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.0.23",port=22,username="root",password="test#Ld&B%Nw23admin")
stdin,stdout,stderr = ssh.exec_command("ifconfig")
result = stdout.read()

ssh.close()
print (result.decode("utf-8"))