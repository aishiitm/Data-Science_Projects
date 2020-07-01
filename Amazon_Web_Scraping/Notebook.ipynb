# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:02:57 2019

@author: aishwarya.kuzhikkat
"""

import requests,time,smtplib
from bs4 import  BeautifulSoup
from notify_run import Notify
from datetime import datetime
url = "https://www.amazon.in/Kadence-Wanderer-Brown-Soprano-Ukulele/dp/B01ALJRCBE/ref=sr_1_4?qid=1572779829&refinements=p_36%3A1318504031&s=musical-instruments&smid=A3HL8HT148CJU9&sr=1-4"
dp = 1800
URL = url
pnmsg = "Below Rs. "+str(dp)+" you can get your Ukulele."
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.select("#productTitle")[0].get_text().strip()
    price = soup.find(id="priceblock_dealprice").get_text()
    main_price = price[2:]
    l = len(main_price)
    if l<=6 :
        main_price = price[2:5]
    else:
        p1 =  price[2]
        p2 =  price[4:7]
        pf = str(p1)+str(p2)
        main_price = int(pf)
    price_now = int(main_price)
    main_price1 = main_price
    print("NAME : "+ title)
    print("CURRENT PRICE : "+ str(main_price1))
    print("DESIRED PRICE : "+ str(dp))
    count = 0
    if(price_now <= dp):
        send_mail()
        push_notification()
    else:
        count = count+1
        print("Rechecking... Last checked at "+str(datetime.now()))
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('myemailid@gmail.com','emailidpassword')
    subject = "Price of Ukulele has fallen down below Rs. "+str(dp)
    body = "Hey Aish! \n The price of Ukulele on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
    msg = f"Subject: {subject} \n\n {body} "
    server.sendmail(
      'myemailid@gmail.com',
    msg
      )
    print("Hey Aish, EMAIL HAS BEEN SENT SUCCESSFULLY.")
 
    server.quit()
def push_notification():
    notify = Notify()
    notify.send(pnmsg)
    print("HEY AISH, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY.")
    print("Check again after an hour.")

count = 0
while(True):
    count += 1
    print("Count : "+str(count))
    check_price()
    time.sleep(300)
