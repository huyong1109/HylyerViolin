# -*- coding: utf-8 -*-
import urllib2, json, os,sys
import re


def youdao(word):
    qword = urllib2.quote(word)
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=HylyerViolin&key=797128576&type=data&doctype=json&version=1.1&q='
    url = baseurl+qword
    resp = urllib2.urlopen(url)
    fanyi = json.loads(resp.read())
    if fanyi['errorCode'] == 0:        
        if 'basic' in fanyi.keys():
            trans = u'%s:\n%s\n%s\n网络释义：\n%s'%(fanyi['query'],''.join(fanyi['translation']),' '.join(fanyi['basic']['explains']),''.join(fanyi['web'][0]['value']))
            return trans
        else:
            trans =u'%s:\n翻译:%s\n'%(fanyi['query'],''.join(fanyi['translation']))        
            return trans
    elif fanyi['errorCode'] == 20:
        return u'对不起，要翻译的文本过长'
    elif fanyi['errorCode'] == 30:
        return u'对不起，无法进行有效的翻译'
    elif fanyi['errorCode'] == 40:
        return u'对不起，不支持的语言类型'
    else:
        return u'对不起，您输入的单词%s无法翻译,请检查拼写'% word


def turling(ask):
	qword = ask
	turlingurl = "http://www.tuling123.com/openapi/api?"
	key = '2b1b183dc6e1a4dd90a1e23c65edbf04'
	url = turlingurl+'key='+key+'&info='+qword
	reply= urllib2.urlopen(url).read()
	re_dict = json.loads(reply)
	text = re_dict['text']
	text = text.replace(";", "\n")
	text = text.replace('<br>','\n',10)
	text = text.replace("#", "\n")
	return  text


def face(img):
	from pprint import pformat
	from facepp import API 
	faceppAPI_KEY = 'db212fa5bc488db66c97808b2c9ef665'
	faceppAPI_SECRET = 'lcv2MD_fMt2FeCyWrG91mZvDxutlu3OM'
	api = API(faceppAPI_KEY, faceppAPI_SECRET)	

	rst = api.detection.detect(url = img)
	gend = {'Male': 0, 'Female': 1}
	peopletile = [["花样少年", "风华正茂", "当立男儿", "不惑壮士"],["豆蔻年华","风姿卓越","风韵犹存","徐娘半老"]]
	def age_stage(age):
		if age <16:
			res = 0
		elif age <30:
			res = 1
		elif age <40:
			res = 2
		else:
			res = 3
		return res
	peopleindex = 1
	reply  = ''
	print  len(rst['face'])
	if len(rst['face']) > 1:
		reply = '别着急，让我喝口水一个一个说\n'
   	for face in rst['face']: 	
		if len(rst['face']) > 1:
			reply += '第'+str(peopleindex)+'位,'
		peopleindex += 1
		gender = face['attribute']['gender']['value']
		age = face['attribute']['age']['value']
		reply +=  '我看您'+ peopletile[gend[gender]][age_stage(age)]+', 心理年龄是'+str(age) +'岁'
		reply += '\n'
	#print_result("Name",rst)
	
	return reply
