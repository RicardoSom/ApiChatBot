import sys
import smtplib

sys.argv.pop(0)
message = ' '.join(sys.argv)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ricardo@devaid.cl', 'ricardo.x92')

server.sendmail('ricardo@devaid.cl', 'vescobar@utem.cl', message.encode("utf8"))

server.quit()