#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

hosturl='http://hub.hust.edu.cn'
posturl='http://hub.hust.edu.cn/hublogin.action'

#use = raw_input("username:\n")

# def checkAllCookiesExist(cookieNameList, cookieJar) :
#     cookiesDict = {};
#     for eachCookieName in cookieNameList :
#         cookiesDict[eachCookieName] = False;
    
#     allCookieFound = True;
#     for cookie in cookieJar :
#         if(cookie.name in cookiesDict) :
#             cookiesDict[cookie.name] = True;
    
#     for eachCookie in cookiesDict.keys() :
#         if(not cookiesDict[eachCookie]) :
#             allCookieFound = False;
#             break;
#     return allCookieFound;

#localcookie
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)
#cj = cookielib.CookieJar();
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
#urllib2.install_opener(opener);

#openweb
h = urllib2.urlopen(hosturl)

headers = {
    'Origin':'http://hub.hust.edu.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    'Referer':'http://hub.hust.edu.cn/index.jsp'
}


#pas = raw_input("password:\n")
pas = '680519'
newpas = base64.b64encode(pas)

sub = '立即登录'

postData = {
    'usertype':'xs',
#    'username':use,
#    'password':newpas,
    'username':'U201214870',
    'password':newpas,
    'submit': sub
}


postData = urllib.urlencode(postData)

request = urllib2.Request(posturl, postData, headers)  
response = urllib2.urlopen(request)

text = response.read()  
print text

response3 = urllib2.urlopen("http://hub.hust.edu.cn/frames/body_left.jsp")
text3 = response3.read()
print text3

response3 = urllib2.urlopen("http://hub.hust.edu.cn/frames/kslogin.jsp?url=http://bksjw.hust.edu.cn/")
response2 = urllib2.urlopen('http://bksjw.hust.edu.cn/aam/slj/WydjksBaoKao_initPage.action?cdbh=631/')
text2 = response3.read()

#print response2.read()
#response3 = urllib2.Request(geturl,None,headers2)

soup = BeautifulSoup(text2)

Key1 = soup.find(name='input', attrs={'name':'key1'})
print Key1
Key1Str = Key1['value']
print Key1Str

Key2 = soup.find(name='input', attrs={'name':'key2'})
Key2Str = Key2['value']
print Key2Str

# HosturlScore = 'http://bksjw.hust.edu.cn/'
# PosturlScore = 'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_queryScore.action'

# #Cookies
# #cj = cookielib.LWPCookieJar()  
# #cookie_support = urllib2.HTTPCookieProcessor(cj)  
# #opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
# #urllib2.install_opener(opener)

# ho = urllib.urlopen(HosturlScore)

# HeadersScore = {
#     'Origin':'http://bksjw.hust.edu.cn',
#     'Referer':'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_readyToQuery.action?cdbh=225',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'
# }
# PostdataScore = {
#     'key1':Key1Str,
#     'key2':Key2Str,
#     'type':'zcj',
#     'stuSfid':'U201214870',
#     'xqselect':'20141'
# }
# PostdataScore = urllib.urlencode(PostdataScore)
# #print PostdataScore
# RequestScore = urllib2.Request(PosturlScore, PostdataScore, HeadersScore)
# ResponseScore = urllib2.urlopen(RequestScore)

# responsescore = ResponseScore.read()
# #print responsescore


