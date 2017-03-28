import requests, re
from bs4 import BeautifulSoup

# url
url = 'http://viewdns.info/reverseip/'


target = raw_input("please enter ip: ")

# Parameters in payload
payload = {'host': target, 't': '1'}


# Setting User-Agent
my_headers = {'User-agent': 'Mozilla/11.0'}

# Getting the response in an Object r
r = requests.get(url, params=payload, headers=my_headers)

#Create a Beautiful soup Object of the response r parsed as html
soup = BeautifulSoup( r.text, 'xml' )

#Getting all h3 tags with class 'r'
h3tags = soup.find_all('td')


w = open("t.txt", 'a')
for i in h3tags:
    try:
        if "ir" in i.string:
            w.write("http://" + i.string + "/administrator" +"\n")
    except:
        continue