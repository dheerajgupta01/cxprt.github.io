# import flask
import smtplib, ssl
from flask import Flask, render_template,request

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')


receiver_email = 'iamanushka.dhiman@gmail.com'

def send_email(receiver_email,name,email,subject,mymsg):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "dheeraj.gupta@greentechits.com"
    password = "znyvomgyfeycozbv"
        
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Try to log in to server and send emailq1
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context) # Secure the connection
    server.ehlo() 
    server.login(sender_email, password)
    SUBJECT = "Testing "
    
    TEXT = 'Name:' + name +' \n' +'Email ID:' +email + ' \n' +'Subject: ' +  subject + ' \n' + 'Message: ' +  mymsg
    
    new_msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            
    server.sendmail(sender_email,[sender_email,receiver_email],new_msg)

@app.route('/', methods =["GET", "POST"])
def getData():
    if request.method == "POST":
      
       your_name = request.form.get("name")
       emailid = request.form.get("email")
       subject = request.form.get("subject")
       mymsg = request.form.get("message")
       
       send_email(receiver_email,your_name,emailid,subject,mymsg)
       
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
    
