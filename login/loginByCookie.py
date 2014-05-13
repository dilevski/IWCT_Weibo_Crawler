# -*- coding: utf8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2, urllib, cookielib, string, json, time

def main():
    req = urllib2.Request(url = "http://weibo.com/")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.802.30 Safari/535.1 SE 2.X MetaSr 1.0')
    cookie = ""#put your cookie here
    req.add_header('Cookie', cookie)
    content = urllib2.urlopen(req).read()
    print content[:3000]
    


main()
