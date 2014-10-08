#!/usr/bin/env python
#-*- coding: utf-8 -*-

import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string
import webbrowser
import os
import re
import base64
from bs4 import BeautifulSoup

hosturl='http://bksjw.hust.edu.cn'
posturl='http://bksjw.hust.edu.cn/hublogin.action'

#cookie
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)

headers = {
    'Origin':'http://bksjw.hust.edu.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    'Referer':'http://bksjw.hust.edu.cn/index.jsp'
}
use = raw_input("username:\n")
pas = raw_input("password:\n")
newpas = base64.b64encode(pas)

sub = '立即登陆'

postData = {
    'usertype':'xs',
    'username':use,
    'password':newpas,
#    'username':'U201214870',
#    'password':newpas,
    'submit': sub
}
postData = urllib.urlencode(postData)

request = urllib2.Request(posturl, postData, headers)  
response = urllib2.urlopen(request)

text = response.read()  
print text

#response2 = urllib2.urlopen('http://bksjw.hust.edu.cn/aam/slj/WydjksBaoKao_initPage.action?cdbh=631/')
#text2 =  response2.read()
#print text2

soup = BeautifulSoup(text)
Key1 = soup.find(name='input', attrs={'name':'key1'})
print Key1
Key1Str = Key1['value']
print Key1Str

picurl = 'http://bksjw.hust.edu.cn/aam/slj/picture.jsp'
pic = urllib2.urlopen('http://bksjw.hust.edu.cn/aam/slj/picture.jsp').read()

with open("D://5.jpg", "wb") as code:     
    code.write(pic)
    
HosturlScore = 'http://bksjw.hust.edu.cn/'
PosturlScore = 'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_queryScore.action'

#Cookies
#cj = cookielib.LWPCookieJar()  
#cookie_support = urllib2.HTTPCookieProcessor(cj)  
#opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
#urllib2.install_opener(opener)

ho = urllib.urlopen(HosturlScore)

HeadersScore = {
    'Origin':'http://bksjw.hust.edu.cn',
    'Referer':'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_readyToQuery.action?cdbh=225',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'
}
PostdataScore = {
    'key1':Key1Str,
    'key2':Key2Str,
    'type':'zcj',
    'stuSfid':'U201214870',
    'xqselect':'20141'
}
PostdataScore = urllib.urlencode(PostdataScore)
#print PostdataScore
RequestScore = urllib2.Request(PosturlScore, PostdataScore, HeadersScore)
ResponseScore = urllib2.urlopen(RequestScore)

responsescore = ResponseScore.read()
#print responsescore
