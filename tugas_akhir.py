import smtplib

sender_email = input(str("Pengirim: "))
rec_email = input(str("Penerima: "))
password = input(str("Masukan kata sandi anda: "))
message = input(str("pesan anda: "))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

print("Login success")
server.sendmail(sender_email, rec_email, object_email, message)
print("Email has been sent to ", rec_email)

