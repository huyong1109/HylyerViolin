# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')

from interface import face
img = IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/1.jpg'
print face(img)

#from interface import youdao
#words = [ 'we are friend' , 'I love you', 'aaaaa', 'please help me to remove the table', 'deske']
#for word  in words:
#	reply = youdao(word)
#	print reply
#
#from interface import turling
#words = [ '你好\n' , '我帅吗','你几岁了','薛定谔定力','笑话','笑话','笑话']
#for word  in words:
#	reply = turling(word)
#	print word
#	print reply
#
