#!/usr/bin/python
# -*- coding: utf-8 -*-
# zabbix notification confirmation script
# python2.7 or above
  
import requests
import json
import os
import sys
  
Toparty = "1"   #部门id
AgentID = 1000002     #应用id

#修改为企业CropID和Secret
CropID = 'ww37d7c999c60b2fa3'
Secret = 'S2etLyLGrvG02IskhC4mFj0Ar7oSYUr89fU5MOhS8bY'
  
#获取Token
Gtoken ="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+ CropID + "&corpsecret=" + Secret
headers = {'Content-Type': 'application/json'}
json_data = json.loads(requests.get(Gtoken).content.decode())
token = json_data["access_token"]
  
#消息发送接口
Purl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
  
#消息发送函数
def msg(title,message):
    weixin_msg = {
         "toparty" : Toparty,
         "msgtype" : "textcard",
         "agentid" : AgentID,
         "textcard" : {
             "title" : title,
             "description" : message,
             "url" : "jk.wiselink.net",
             "btntxt":"更多"
          }
      }
    print requests.post(Purl,json.dumps(weixin_msg),headers=headers)
  
if __name__ == '__main__':
    title = sys.argv[1]        #获取第一个参数
    message = sys.argv[2]      #获取第二个参数
    msg(title,message)

