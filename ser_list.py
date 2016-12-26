#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import paramiko

dic = {
    "root":[
        "192.168.0.23",
        "192.168.0.1",
        "192.168.0.100",
        ],
        "eric":[
            "192.168.0.23",
        ]
}
host_list = dic["root"]

print ("Please select:")
for index,item in enumerate(host_list,1):
    print (index,item)
inp = input("You select (No):")
inp = input(inp)
hostname = host_list[inp-1]
port = 22

tran = paramiko.Transport((hostname,port,))
tran.start_client()
default_path = os.path.join(os.environ["HOME"],".ssh","id_rsa")
key = paramiko.RSAKey.from_private_key_file(default_path)
tran.auth_publickey("jason", key)

chan = tran.open_session()
chan.get_pty()
chan.invoke_shell()

chan.close()
tran.close()





