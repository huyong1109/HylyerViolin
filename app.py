# -*- coding: utf-8 -*-
import os,sys

reload(sys)
sys.setdefaultencoding('utf-8')


import unicodedata
from flask import Flask
from flask.ext.werobot import WeRoBot
from werobot.client  import Client




app = Flask(__name__)
robot = WeRoBot(app, token = "waiter1109", rule = '/test')

mywxid = "wx088f6d071740acfc"
mywxsecret = "524a1ebcc15b4e4f27c66f02f071c5ff"



@robot.subscribe
def echo(message):
    return '你好！ 欢迎关注逸筠提琴!'

@robot.unsubscribe
def echo(message):
    return '舍不得跟你分开'

import 	re

@robot.filter(re.compile('^[a-zA-Z]+'))
def echo(message):
   	from werobot.reply import TextReply
	from interface import youdao
	fanyi= youdao(message.content)
	reply = TextReply(message=message, content=''+fanyi)
	return reply

@robot.filter(re.compile(u'.*音乐.*'))
def echo(message):
	return [
        "微信你不懂爱",
        "龚琳娜最新力作",
        "http://weixin.com/budongai.mp3",
        ]

@robot.text
def echo(message):
   	from werobot.reply import TextReply
	from interface import turling 
	robotrep = turling(message.content)
	#robotrep = turling('你好')
	reply = TextReply(message=message, content=robotrep)
	return reply

@robot.image
def echo(message):
    from werobot.reply import ArticlesReply, Article 
    from interface import face 

    reply = ArticlesReply(message=message)
    article = Article(
        title = "智能测试心理年龄",
        description = face(message.img),
        img = message.img,
        url = "http://mp.weixin.qq.com/s?__biz=MzIwNjE2Mjg5NA==&mid=402671317&idx=1&sn=5abcb6337a32d66248cfd06504c29401#rd"
    )
    reply.add_article(article)
    return reply
    
#client = Client(mywxid, mywxsecret)
#client.create_menu({
#    "button":[
#        {
#            "type":"click",
#            "name":"今日歌曲",
#            "key":"V1001_TODAY_MUSIC"
#        },
#        {
#            "type":"click",
#            "name":"歌手简介",
#            "key":"V1001_TODAY_SINGER"
#        },
#        {
#            "name":"菜单",
#            "sub_button":[
#                {
#                    "type":"view",
#                    "name":"搜索",
#                    "url":"http://www.soso.com/"
#                },
#                {
#                    "type":"view",
#                    "name":"视频",
#                    "url":"http://v.qq.com/"
#                },
#                {
#                    "type":"click",
#                    "name":"赞一下我们",
#                    "key":"V1001_GOOD"
#                }
#            ]
#        }
#    ]})
