#coding:gbk
import urllib2,sys,re,MySQLdb,string

#reload(sys)
#sys.setdefaultencoding('gbk')

c=MySQLdb.connect(host='localhost',user='root',passwd='humiao',db='lsh',charset='utf8')
if not c:
    print 'Error'
cur=c.cursor()

print '*** Deleting some data'
cur.execute('DELETE FROM movie4')
print '***Input n'
n=input()
process=0
#http://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=10&page_start=0
#request0=urllib2.Request(url="http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=10&page_start=0")
print '***Initialize succeeded'
request0=urllib2.Request(url="http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit="+'%d'%n+"&page_start=0")
result0=urllib2.urlopen(request0).read()
#print result0
#print len(result0)
print '***Geting listofurl'
url=re.compile(r'url".+?".+?playable')
listofurl=url.findall(result0)  
for i in listofurl:
    i=i[6:-11]
    i=i.replace("\\",'')
    #print i
print '***processing...'
#print len(listofurl)
for j in range(0,len(listofurl)):
    process=process+1
    print process
    request=urllib2.Request(url=listofurl[j][6:-11].replace("\\",''))
    result=urllib2.urlopen(request).read()
    #print result

    imglocation=re.compile(r'<img src=".+?".+?title')
    listofimglocation=imglocation.findall(result)
    #print listofimglocation[0][10:-7]

    moviename=re.compile(r'keywords".+?".+?,')
    listofmoviename=moviename.findall(result)
    #print listofmoviename[0][19:-1]

    director=re.compile(r'directedBy".+?</a>')
    listofdirector=director.findall(result)
    #for i in listofdirector:print i[12:-4]
    listofdir=listofdirector[0][12:-4]
    '''for i in range(1,len(listofdirector)):
        listofdir=listofdir+'/'+listofdirector[i][12:-4]'''
    #print listofdir    
    
    actor=re.compile(r'v:starring.+?</a>')
    listofactor=actor.findall(result)
    #for i in listofactor:print i[12:-4]
    listofact=listofactor[0][12:-4]
    '''for i in range(1,len(listofactor)):
        listofact=listofact+'/'+listofactor[i][12:-4]'''
    #print listofact   

    print '***saving data'
#for i in range(0,n):
    #print listofmoviename[0][19:-1],listofdir,listofact,listofimglocation[0][10:-7]
    cur.execute("INSERT INTO movie4 VALUES('%s','%s','%s','%s')"%(listofmoviename[0][19:-1],listofdir,listofact,listofimglocation[0][10:-7]))
    #print process

print '=====***Finished***====='
cur.execute('SELECT * FROM movie4')
for data in cur.fetchall():
    print '%s\t%s\t%s\t%s' % data
cur.close()
c.commit()
c.close()

#print result
#haha=raw_input("Click enter key to exit.")
