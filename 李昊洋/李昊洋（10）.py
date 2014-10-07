import re, urllib,urllib2
for i in range(20):
    myUrl = "http://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start="+str(i*20)+"&type=T"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
    headers = { 'User-Agent' : user_agent }   
    req = urllib2.Request(myUrl, headers = headers)   
    myResponse = urllib2.urlopen(req)  
    myPage = myResponse.read()
    unicodePage = myPage
    for g in range(20):
        
        
        myItems1 = re.findall('<a href=.*? title="(.*?)"', unicodePage,re.S)
        print myItems1[g]
        
        myItems2 = re.findall('<div class="pub">(.*?)</div>', unicodePage,re.S)
        print myItems2[g]
        myItems3 = re.findall('<p>(.*?)</p>', unicodePage,re.S)
        print myItems3[g]
        f= open('book.txt','a')
        f.write(myItems1[g])
        f.write(myItems2[g])
        f.write(myItems3[g])
        
                       
  
    
