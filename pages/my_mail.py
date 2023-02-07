import smtplib,ssl



def send_mail(message):
        host = "smtp@gmail.com"
        ports = 465

        username = "niranjansaini502@gmail.com"
        password = "jlboytkgxshmgxoa"

        my_context = ssl.create_default_context()

        reciver = "niranjansaini502@gmail.com"

        with smtplib.SMTP_SSL(host,ports,context=my_context) as server :
            server.login(username,password)
            server.sendmail(username,reciver,message)





