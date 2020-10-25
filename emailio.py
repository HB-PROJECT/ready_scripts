import smtplib, ssl

from sys import argv

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "email"
receiver_email = argv[1]
password = "password"
code = argv[2]


# python email_io.py receiver_email code

# message = """
# <p><h1><b><font color = "blue>Enter this code</font></b></h1></p>
# <br><br>
# <p><h2><b><font color = "red>{}</font></b></h2></p>
# """.format(code)


message = """
Enter this code : {}
""".format(code)

print(f"receiver : {receiver_email}\ncode : {code}")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,message)

