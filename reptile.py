# coding=utf-8

import urllib,urllib2
import re

page = raw_input("请输入网址")
url = page + "?see_lz=1"
pattern = urllib2.urlopen(url).read()

title = re.search(r"<title>(.*)</title>",pattern)
body = re.search(r"吾王所指，剑锋所向！<br>(.*)</div><br>"
                 ,pattern)
print title.group(1)

temp = re.sub(r'<br><br>','\n',body.group(1))
content = re.sub(r'垩','',temp)
print content
print "finish"
