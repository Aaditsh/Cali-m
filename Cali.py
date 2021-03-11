import smtplib

print("I am Cali the multi purpose software ")
print("Version 2021.3.10")
print("  ")
print("For Autometic mail sender type mail")

mailin = str(input())

if mailin == "mail":
    print("The Email id of reciver")
    rec = input()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your email here', 'password here')
    server.sendmail('pythonmodmail@gmail.com',
                     rec ,
                    'Hi i am python mod mail made by sir Aadit sharma we are testing this so kindly provide feedback')
                      



            


