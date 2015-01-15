#!/usr/bin/env python
# coding=utf-8
# jetson@2014-12-19 15:23:47
import urllib2
import re
#基地址
baseurl = 'http://tieba.baidu.com/f/good?kw=%E6%B0%B8%E5%A4%9C%E5%90%9B%E7%8E%8B&ie=utf-8&cid=4&pn='


def getUrl(baseurl):
    '''this function will get all the url of
       txt page in tieba base on baseurl. 
    '''
    
    #小说内容帖子号
    page_number = []

    #小说内容url
    source_url1 = 'http://tieba.baidu.com'
    source_url2 = '?see_lz=1'

    #url仓库
    url_warehouse = []

    pattern = re.compile('/p/\d+') 
	
    for offsize in range(5):	
        url = baseurl + str(offsize*50)

        content = urllib2.urlopen(url).read()
   
        page_number = re.findall(pattern,content)
        for i in page_number:
            url_full = source_url1 + i + source_url2
            if url_full not in url_warehouse:
                url_warehouse.append(url_full)


    print '%d urls has got'%len(url_warehouse)
    return url_warehouse

if __name__=='__main__':
    a = getUrl(baseurl)
    if len(a) > 1:
        print 
    print a

