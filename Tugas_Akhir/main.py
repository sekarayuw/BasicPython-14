import smtplib

# SETUP EMAIL LOGIN 
email_pengguna = input(str("Masukkan akun gmail: "))
kata_sandi = input(str("Masukkan password gmail: "))

# SETUP PENERIMA EMAIL
with open('receiver_list.txt', 'r') as file:
	penerima = file.read().replace('\n', ',')

# SETUP Pengirim, penerima, judul dan isi email
email_pengirim = email_pengguna
email_penerima = input(str("Masukkan email penerima: "))
subject_email = input(str("Masukkan  subjek atau judul: "))
pesan_email = input(str("Masukkan pesan: "))

email_text = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (email_pengirim, ", ".join(email_penerima), subject_email, pesan_email)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email_pengguna, kata_sandi)
    server.sendmail(email_pengirim, email_penerima, email_text)
    server.close()

    print('Email berhasil terkirim!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
	
"""
referensi:
   1. https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
   2. https://windows10review.blogspot.com/2021/06/dwonload-code-python-to-send-email.html
"""