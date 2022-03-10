from flask import Flask, request
from firebase_admin import credentials, initialize_app, db, auth
import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from test import read_interviewer, get_empty, get_intersections

ia1 = read_interviewer('Files/IA1.csv')
ia2 = read_interviewer('Files/IA2.csv')
ia3 = read_interviewer('Files/IA3.csv')

ia1_empty = get_empty(ia1)
ia2_empty = get_empty(ia2)
ia3_empty = get_empty(ia3)

common_a = get_intersections(ia1_empty, ia2_empty, ia3_empty)

ib1 = read_interviewer('Files/IB1.csv')
ib2 = read_interviewer('Files/IB2.csv')
ib3 = read_interviewer('Files/IB3.csv')

ib1_empty = get_empty(ib1)
ib2_empty = get_empty(ib2)
ib3_empty = get_empty(ib3)

common_b = get_intersections(ib1_empty, ib2_empty, ib3_empty)
 
N = 7
app = Flask('app')

cred = credentials.Certificate("InterviewNowCred.json")
dataapp = initialize_app(cred, {"databaseURL":"https://interview-now-dc764-default-rtdb.asia-southeast1.firebasedatabase.app/"})
ref = db.reference('/')

def send_email(userid, receiver_email, name):
  sender_email = "ctrlaltelitecrce@gmail.com"
  password = "ctrlaltelitecrce50"
  msg=MIMEMultipart()
  msg['From']=sender_email
  msg['To']=receiver_email
  msg['subject']='Credentials for Interview Now'
  body = f"""
  Your Credentials to access the Interview Now portal
  Username : {receiver_email}
  Password : {userid}

  This is an auto generated email by Interview Now.
  Do not reply to this mail.
  """
  msg.attach(MIMEText(body,'plain'))
  mail=smtplib.SMTP('smtp.gmail.com',587)
  mail.ehlo()
  mail.starttls()
  mail.login(sender_email, password)
  text=msg.as_string()
  mail.sendmail(sender_email, receiver_email, text)
  mail.quit()

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

@app.route('/adduser', methods=['POST'])
def adduser():
  data = request.get_json()
  name = data['name']
  email = data['email']
  pwd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
  user = auth.create_user(
    email = email,
    email_verified=False,
    password= pwd,
    display_name=name,
    phone_number = "+11111111111",
    disabled=False
  )
  uid = user.uid
  send_email(uid, email, name)
  return {}

@app.route('/webhook', methods=['POST'])
def webhook():
  data = request.get_json()
  name = data['queryResult']['parameters']['person']['name']
  role = data['queryResult']['parameters']['Interviewee_Role']
  company = data['queryResult']['parameters']['company']
  print(name, role, company)
  return {}
  
@app.route('/getdata', methods=['GET'])
def getdata():
  return json.dumps(ref.get())

@app.route('/updatedb', methods=['POST'])
def updatedb():
  data = request.get_json()
  email = data["email"]
  status = int(data["status"])
  uid = data['uid']
  interviewer = ref.get()[email]
  if(status==1):
    schedule_meet()
  ref.child(f'/users/{uid}').set({
    interviewer: status
  })
    


  
app.run(host='0.0.0.0', port=8080)

