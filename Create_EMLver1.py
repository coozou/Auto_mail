#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:59:12 2019

@author: shinozakiryo
"""

import email
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email import generator






#-------------------------------
# 宛先アドレスの読み込み
a = open("mail_address.txt", "r", encoding="ISO-2022-JP")
a1 = a.readlines()
a2 = ",".join(a1)
address = a2.replace("\n", "")

#print(address)

a.close()
#-------------------------------
# メール件名の読み込み
t = open("title.txt", "r", encoding="utf-8")
title = t.read()

#print(title)

t.close()
#-------------------------------
# お名前（メール本文）の読み込み
n = open("customer_name.txt", "r", encoding="ISO-2022-JP")
name = n.read()

#print(name)

n.close()
#-------------------------------
#メール本文の読み込み
h = open("mail_body.txt", "r", encoding="ISO-2022-JP")
honbun = h.read()

#print(honbun)

h.close()



#honbun = """
#NTT Com篠崎です。お世話になっております。
#本日はありがとうございました。
#"""
#-------------------------------


from_addr = 't.numajiri@ntt.com'
to_addr = address
subject = title
body = name + "\n" + " \n" +" \n" + honbun


encoding = 'utf-8'
sender_name = Header('Takashi Nukajiri', encoding).encode()

message = MIMEText(body.encode(encoding), 'plain', _charset=encoding)
message['Subject'] = Header(subject, encoding)
message['From'] = formataddr((sender_name, from_addr))
message['To'] = to_addr
message.add_header('X-Unsent', '1')

with open('Mail01.eml', 'w') as eml:
    gen = generator.Generator(eml)
    gen.flatten(message)

print("** 作成完了 **")
