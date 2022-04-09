import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

pengirim = 'rifqifai@gmail.com' ##diisi Email Pengirim
penerima = 'anrzero@gmail.com' ##diisi Email Penerima
msg = MIMEText("isi email") ##Isi Email
msg['Subject'] = 'Mengirim email via python [122]' ##Subject Email
msg['From'] = pengirim
msg['To'] = penerima

msg = MIMEMultipart()
msg.attach(MIMEText(file("rifqi.txt").read()))

pwd = 'password' ##diisi Password Pengirim
s = smtplib.SMTP_SSL()
s.connect('smtp.gmail.com', 465)
s.login(pengirim, pwd)
s.sendmail(pengirim, penerima, msg.as_string())
s.quit()