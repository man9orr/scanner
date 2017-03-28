#!/usr/bin/python
import time
from bs4 import BeautifulSoup
import urllib
import mechanize
import os

# page = urllib.urlopen("http://109.123.90.187/joomlatest/administrator")
# login = BeautifulSoup(page.read(), "lxml")
#
# print page.code

error = ["Username and password do not match or you do not have an account yet." , "LADP"]
sussuc = "Control Panel"
br = mechanize.Browser()
br.set_handle_robots(False)
fopen = open("/root/t/python/scanner_project/scanner/t.txt", "r")

for line in fopen.readlines():
    print line.strip()

    try:
        page = br.open(line, timeout=5)
        print "no error"
        print page.code

    except:
        # print page.code
        pass
    try:
        for form in br.forms():


            br.select_form(nr=0)
            br.form["username"] = "administrator"
            br.form["passwd"] = "123456"
            br.submit()
            readingPage = br.response().read()
            for n in error:
                if n in readingPage:
                    print "wrong credential"
            if sussuc in readingPage:
                print "succeffuly loged in"

    except:
            pass

fopen.close()






