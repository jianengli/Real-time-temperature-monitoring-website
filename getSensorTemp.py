from obtainWeatherInfo import ObtainWeatherInfo
import os
import glob
import time
import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE

weatherInfo = ObtainWeatherInfo()
currentTemp = weatherInfo.get_current_temp()

os.system("modprobe w1_gpio")
os.system("modprobe w1_therm")

devicelist = glob.glob("/sys/bus/w1/devices/28*")
devicefile = devicelist[0]+"/w1_slave"

SENDER = 'junweigong0571@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
USER_ACCOUNT = {'username': '...@gmail.com', 'password': '...'}
receivers = ['...@gmail.com']

def sendEmail(wrong_item, tempertature, curTime):
    msg_root = MIMEMultipart()
    msg_root['Subject'] = "Sensor alert(no-reply)"
    msg_root['To'] = COMMASPACE.join(receivers)
    text = "In {}, the temperature detected by sensor is {}, there may be {}.".format(curTime, tempertature, wrong_item)
    msg_text = MIMEText(text, 'html', 'utf-8')
    msg_root.attach(msg_text)

    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(USER_ACCOUNT['username'], USER_ACCOUNT['password'])
    smtp.sendmail(SENDER, receivers, msg_root.as_string())

while True:
    fileobj = open(devicefile, 'r')

    lines = fileobj.readlines()
    fileobj.close()

    # print lines[0][:-1]
    # print lines[1][:-1]

    tempdata = lines[1].split("=")

    sensorTemp = float(tempdata[1])

    sensorTemp = sensorTemp/1000

    wrong = ""

    if currentTemp < 10:
        if sensorTemp < -10 or sensorTemp > 35:
            wrong = "sensor wrong"
        elif -10 < sensorTemp < 0:
            wrong = "heating wrong"
        else:
            wrong = ""

    elif currentTemp > 25:
        if sensorTemp < -10 or sensorTemp > 35:
            wrong = "sensor wrong"
        elif 28 < sensorTemp < 30:
            wrong = "colding wrong"
        else:
            wrong = ""

    else:
        if sensorTemp < -10 or sensorTemp > 35:
            wrong = "sensor wrong"
        else:
            wrong = ""

    now_date_time = datetime.datetime.now()
    date= now_date_time.strftime("%Y-%m-%d")
    date_time = now_date_time.strftime("%H:%M:%S")

    if len(wrong) != 0:
        sendEmail(wrong, sensorTemp, date+" "+date_time)
        print(wrong+" "+str(currentTemp)+" "+str(sensorTemp)+" "+date+" "+date_time)
    else:
        url = "http://130.243.35.86/lab5/receiveTemp.php?date="+date+"&time="+date_time+"&temperature="+str(sensorTemp)
        #parameter = {"date": date, "time": date_time, "temperature": sensorTemp}
        r = requests.get(url)
        print(url)

    time.sleep(5)


