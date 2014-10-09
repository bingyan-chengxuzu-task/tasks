#! /usr/bin/env python
# Author: DY.HUST
# Date: 2014/10/06
# Description: a interpreter for markdown

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re

class __interpreter():

	def __init__(self):
		self.result = ''
		self.rawlist = []
		self.linkReference = []
		self.linkDict = {}

	def __beg(self, tag):
		return '<' + tag + '>'
	def __end(self, tag):
		return '</' + tag + '>\n'
	def write(self, strbuff):
		self.result += strbuff

	def __countLChar(self, line, c):
		cnt = 0
		for get in line:
			if c!=get: 
				break
			cnt += 1
		return cnt

	def __delLTab(self, line):
		limit = min(4, len(line))
		cnt = self.__countLChar(line[:limit], ' ')
		return line[cnt:]

	def __delHead(self, line):
		tag = self.handleHead(line)
		line = self.__delLTab(line)
		if 'ul'==tag:
			return line[2:].lstrip(' ')
		elif 'ol'==tag:
			return line[line.find('.')+1:].lstrip(' ')
		elif 'blockquote'==tag:
			return line[1:]
		else :
			return line

	def __replace(self, string):
		# the 1st line must run before 2rd line
		# becasue there is a '&' in '&amp;'
		string = string.replace('&', '&amp;')
		string = string.replace('<', '&lt;')
		return string

#--------------------------------------------------------------#

	def interpret(self, raw):
		# replace tab with for blank, and handling can be easier 
		raw = raw.replace('\t', '    ')
		import StringIO
		rawIO = StringIO.StringIO(raw)
		self.rawlist = [line for line in rawIO.readlines()]

		self.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
		self.write(self.__beg('html') + '\n')
		self.write(self.__beg('body') + '\n')
		self.interBlock(self.rawlist)
		# write the link and image
		self.writeReference()
		self.write(self.__end('html'))
		self.write(self.__end('body'))
		# print for debuging, delete after
		# print self.result
		return self.result

	def interBlock(self, strList):
		listLen = len(strList)
		pos = 0
		# judge which types the line is, and get a call-back funtion
		# each call-back funtion handle the different scope for each type 
		while pos < listLen :
			tag = self.handleHead(strList[pos])
			matchLines = {'code':self.matchCode,
						'\n':self.matchEnter,
						'blockquote':self.matchQuote,
						'p':self.matchParagraph,	
						'atx':self.matchAtx,
						'hr':self.matchCutline,
						'ul':self.matchList,
						'ol':self.matchList,
						}[tag]
			pos += matchLines(strList[pos:])

#--------------------------------------------------------------#

	def matchEnter(self, strList):
		return 1

	def matchCutline(self, strList):
		self.write(self.__beg('hr'))
		return 1

	def matchAtx(self, strList):
		line = strList[0].lstrip().rstrip()
		tag = 'h' + str(self.__countLChar(line, '#'))
		line = line.lstrip('#').rstrip().rstrip('#')
		self.write(self.__beg(tag) + self.interString(line) + self.__end(tag))
		return 1

	# count the available line through the funtion 'rule'
	def __countLine(self, strList, rule):
		cnt = 0
		for line in strList :
			if rule(line) :
				cnt += 1
			else :
				break
		return cnt

	def matchCode(self, strList):
		def rule(line) :
			tag = self.handleHead(line)
			return 'code'==tag or '\n'==tag
		cnt = self.__countLine(strList, rule)
		self.write(self.__beg('pre') + self.__beg('code'))

		# delete four blank
		listBuff = map(self.__delLTab,strList[:cnt])
		# coz "__replace" can't be called in other place for this situation
		listBuff = map(self.__replace,listBuff)
		map(self.write, listBuff)

		self.write(self.__end('code') + self.__end('pre'))
		return cnt

#--------------------------------------------------------------#

	# count the available line
	def __countQuote(self, strList):
		enterFlag = 0
		cnt = 0
		for line in strList:
			tag = self.handleHead(line)
			if 'blockquote'==tag:
				cnt += 1
			elif '\n'==tag:
				enterFlag += 1
				cnt += 1
			elif 'p'==tag and 0==enterFlag:
				cnt += 1
			else :
				break
		return cnt

	def matchQuote(self, strList):
		cnt = self.__countQuote(strList)

		self.write(self.__beg('blockquote'))
		# handle the nested block through recursion
		strList = map(self.__delHead, strList[:cnt])
		self.interBlock(strList[:cnt])
		self.write(self.__end('blockquote'))
		return cnt

#--------------------------------------------------------------#

	def is_setext(self, line):
		line = self.__delLTab(line)
		head = line[0]
		if '-'!=head and '='!=head:
			return 'p'
		# there is no other char in a setest line but for '\n', '-', '='
		for c in line:
			if '\n'!=c and head!=c:
				return 'p'
		return {'=':'h1','-':'h2'}[head]

	# note: recursion will stop here
	def matchParagraph(self, strList):
		def rule(line) :
			return 'p'==self.handleHead(line)
		cnt = self.__countLine(strList, rule)

		# make several lines into a single line
		listBuff = [line.lstrip() for line in strList[:cnt]]
		string = reduce(lambda s1,s2:s1+s2, listBuff)

		# handle the inline element
		string = self.interString(string)

		# setext
		tag = 'p'
		if '\n'!=strList[cnt-1] and cnt < len(strList) :
			tag = self.is_setext(strList[cnt])
		if 'h1'==tag or 'h2'==tag:
			cnt += 1
		self.write(self.__beg(tag) + string + self.__end(tag))
		return cnt

#--------------------------------------------------------------#

	# just count lines for a single part of whole list
	def __countListPart(self, strList, listTag):
		isNextPart = False
		enterFlag = 0
		isParagraph = False
		cnt = 0
		for line in strList:
			tag = self.handleHead(line)
			if listTag==tag :
				if isNextPart:
					break
				isNextPart = True
				cnt += 1
			elif '\n'==tag:
				enterFlag += 1
				cnt += 1				
			elif 'p'==tag and 0==enterFlag:
				cnt += 1
			elif self.__countLChar(line, ' ') >= 4:
				enterFlag = 0
				cnt += 1
			else:
				break
			if listTag!=tag and 'p'!=tag :
				isParagraph = True
		return isParagraph, cnt

	'''
	1. xxx
	2. xxx	# do not use the <p></p> tag
	
	1. xxx

	2. xxx 	# use the <p></p> tag
	'''	
	def __delParagraphTag(self, findPos):
		resPos = self.result.find(self.__beg('p'), findPos)
		if -1==resPos:
			return
		self.result = self.result[:resPos] + self.result[resPos+len(self.__beg('p')):]
		resPos = self.result.rfind(self.__end('p'))
		if -1==resPos:
			return
		self.result = self.result[:resPos] + self.result[resPos+len(self.__end('p')):]

	def matchList(self, strList):
		listTag = self.handleHead(strList[0])
		self.write(self.__beg(listTag))
		pos = 0
		posForPara = len(self.result)
		isParagraph = False
		paraIndex = 0
		isLastParagraph = False		# is delete the <p></p> tag ?
		while pos < len(strList):
			if listTag != self.handleHead(strList[pos]):
				break
			isLastParagraph = isParagraph
			paraIndex += 1
			isParagraph, index = self.__countListPart(strList[pos:], listTag)
			posForPara = len(self.result)

			self.write(self.__beg('li'))
			newList = map(self.__delHead, strList[pos:pos+index])
			# handle the nested block through recursion
			self.interBlock(newList)
			self.write(self.__end('li'))

			pos += index
			if not isParagraph :
				self.__delParagraphTag(posForPara)
		if 1==paraIndex :
			isLastParagraph = isParagraph
		if not isLastParagraph:
			self.__delParagraphTag(posForPara)
		self.write(self.__end(listTag))
		return pos
		
#--------------------------------------------------------------#
	
	def is_cut_line(self, line, symbol):
		cnt = 0
		for c in line:
			if ' ' == c:
				continue
			elif symbol == c:
				cnt += 1
			else :
				break
		return True if cnt>=3 else False

	def handleHead(self, line):
		if self.__countLChar(line, ' ')>=4 : 
			return 'code'
		line = self.__delLTab(line)
		head = line[0]
		if '\n'==head:
			return '\n'
		elif '>'==head:
			return 'blockquote'
		elif '#'==head:
			return 'atx'
		elif '*'==head:
			if self.is_cut_line(line, '*'):
				return 'hr'
			elif -1!=line.find(' ', 1, 2) :
				return 'ul'
		elif '-'==head:
			if self.is_cut_line(line, '-'):
				return 'hr'
			elif -1!=line.find(' ', 1, 2) :
				return 'ul'
			elif self.is_setext(line):
				return 'setext'
		elif '='==head:
			if self.is_setext(line):
				return 'setext'
		elif '_'==head:
			if self.is_cut_line(line, '-'):
				return 'hr'
		elif '+'==head:
			if -1!=line.find(' ', 1, 2):
				return 'ul'

		# ordered list
		pos = line.find('.')
		if -1!= pos:
			if line[:pos].isdigit():
				return 'ol'
			
		return 'p'

#--------------------------------------------------------------#
	def interString(self, string):
		string = self.__replace(string)
		strLen = len(string)
		pos = 0
		buff = ''
		# judge which types the char is, and get a call-back funtion
		# each call-back funtion handle the different scope for each type 
		while pos < strLen:
			matchChar = {'*': self.emphasis,
					'_': self.emphasis,
					'`': self.lineCode,
					'[': self.link_debug,
					'!': self.link_debug,
					'\\': self.trans,
					'\n': self.enter,
			}.get(string[pos], self.char)
			strGet, index = matchChar(string[pos:])
			pos += index
			buff += strGet
		return buff
	
	# *xxxx* **xxxx** -xxxx- -xxxx-
	def emphasis(self, string):
		head = string[0]
		cnt = self.__countLChar(string, head)
		head *= min(cnt, 2)
		tag = {'*':'em', '**':'strong', '_':'em', '__':'strong',}[head]
		index = string.find(head, cnt)
		if -1 == index :
			return string[0], 1
		buff = self.__beg(tag) + string[cnt:index].replace('\n', '') + self.__end(tag)
		return buff, index+cnt

	# i'm lazy to pack the two funtion into one
	def lineCode(self, string):
		head = string[0]
		cnt = self.__countLChar(string, head)
		head *= cnt
		index = string.find(head, cnt)
		if -1 == index :
			return string[0], 1
		buff = self.__beg('code') + string[cnt:index].replace('\n', '') + self.__end('code')
		return buff, index+cnt
	
	def trans(self, string):	# \\
		if len(string) >= 2:
			return string[1], 2
		else :
			return '', 1
	def char(self, string):		# normal char
		return string[0], 1
	def enter(self, string):
		return '', 1

#--------------------------------------------------------------#

	# call this funtion at last
	def writeReference(self) :
		for linkID, url, title in self.linkReference:
			lenIDstr = len ('&['+linkID+']&')
			pos = self.result.find('&['+linkID+']&')
			content, linkType = self.linkDict.get(linkID, ('',''))
			if '' == content :
				continue
			totalLink = self.makeTotalLink(url, title, content, linkType)
			self.result = self.result[:pos] + totalLink + self.result[pos+lenIDstr:]

	def makeTotalLink(self, url, title, content, linkType):
		buff = ''
		if 'image'==linkType :
			buff = '<img src="' + url + '" alt="' + content + '"'
			if ('' != title) :
				buff += 'title="' + title +'"'
			buff += '>'
		elif 'link'==linkType:
			buff = '<a href="' + url + '"'
			if '' != title :
				buff += 'title="' + title + '"'
			buff += '>' + content + "</a>"
		return buff

	def link_debug(self, string):
		# ![content]
		linkType = {'!':'image', '[':'link',}[string[0]]
		# []( or []: or [][
		restr = r'''
				!?			# !
				\[			# [
				([^\]]+)	# content 1
				\]			# ]
				([[:(])		# [ or : 
				'''
		matchObj = re.match(restr, string, re.X)
		if None == matchObj:
			return string[0], 1
		content = matchObj.group(1)
		mode = {'(':'inline', '[':'get_refer', ':':'set_refer',}[matchObj.group(2)]
		pos = len(matchObj.group()) - 1

		if 'inline'==mode :
			totalLink, postemp = self.inlineLink(string[pos:], content, linkType)
			if ''!=totalLink :
				return totalLink, pos + postemp
		elif 'set_refer'==mode:
			flag, postemp = self.setReference(string[pos:], content)
			if not flag:
				return '', pos + postemp
		elif 'get_refer'==mode:
			linkMark, postemp = self.getReference(string[pos:], content, linkType)
			if ''!=linkMark:
				return linkMark, pos + postemp
		return '', 1

	# [content]( url "title")
	def inlineLink(self, string, content, linkType):
		restr = r'''
			\(			# (
			([^)"]+)	# url 1
			(			# 2
			["]			# " 
			([^"]+)		# title 3
			["]			# "
			)			
			?			# optional
			\)			# )
			'''
		matchObj = re.match(restr, string, re.X)
		if None == matchObj:
			return '', 0
		url = matchObj.group(1)
		title = matchObj.group(3) if None!=matchObj.group(3) else ''
		return self.makeTotalLink(url, title, content, linkType), len(matchObj.group())

	# [linkID]: <url> (title) # [linkID]: url (title) # () '' ""
	def setReference(self, string, linkID) :
		restr = r'''
			:			# :
			[ ]*		# blank
			(&lt;)?		# < optional 1
			([^>\s]+)	# url 2
			>?			# >
			\s*			# space and tab
			(			# 3
			['("]		# ' ( "
			([^')"]+)	# title 4
			[')"]		# ' ) "
			)?
			'''
		matchObj = re.match(restr, string, re.X)	
		if None == matchObj:
			return True, 1
		url = matchObj.group(2)
		title = matchObj.group(4) if None!=matchObj.group(4) else ''
		self.linkReference.append((linkID, url, title))
		return False, len(matchObj.group())

	# [cotent][linkID]
	def getReference(self, string, content, linkType):
		restr = r'''
				\[		# [
				([^]]*)	# LinkID 1
				\]		# ]
				'''
		matchObj = re.match(restr, string, re.X)	
		if None == matchObj:
			return '', 1
		linkID = matchObj.group(1)
		if '' == linkID :
			linkID = content
		self.linkDict[linkID] = content, linkType
		return '&['+ linkID +']&', len(matchObj.group())

#--------------------------------------------------------------#

def interMarkdown(raw):
	return __interpreter().interpret(raw)
'''
fi = open('/home/user/data.in', 'r')
fo = open('/home/user/data.html', 'w')


result = __interpreter().interpret(fi.read())
fo.write(result)
'''


