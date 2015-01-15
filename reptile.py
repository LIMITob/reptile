#!/usr/bin/env python
# coding=utf-8
# jetson@2014-12-17 16:47:34
import urllib2
import re


def grap1page(url):
    '''
    grap the page of input url and store
    txt resource in file
    '''
    # title match pattern
    tp = re.compile('<title>.*</title>')
    # body match pattern
    bp = re.compile('<cc>.*</div><br></cc>')

    content = urllib2.urlopen(url).read()
    title = re.search(tp, content)
    body_list = re.findall(bp, content)
    body = ''

    # graped content handling
    title = re.sub('[\w<>/]', '', title.group())

    print 'title :', title

    for i in body_list:
        i = i.replace('<br>', '\n')
        body += i
    print body

    a = open(title + '.txt', 'w')
    a.write(body)
    a.close()


if __name__ == '__main__':
    grap1page('http://tieba.baidu.com/p/3110396889?see_lz=1')
