#Amazon Custom Watchlist
from bs4 import BeautifulSoup
import time
import requests

def check_price(): 

    #Change the URL with the URL of the product you want
    URL = 'https://www.amazon.in/dp/B07GR2NPM1/?coliid=IA4V2UGVW893N&colid=3FHOIQU9O3GDL&psc=1&ref_=lv_ov_lig_dp_it'

    #Go to your browser and search User agent. Copy the result to the useragent here
    headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title = (soup.find(id="productTitle").getText()).strip()
    #Stip and remove unnecessary characters from the price variable
    price = int(soup.find(id="priceblock_ourprice").get_text()[1:8].replace(",",""))


    print(price,title)
    #set the limit under which you need to get email
    if(price < 80000):
        send_mail(price,URL,title)

def send_mail(price,URL,title):
    import smtplib

    #Creating a smtp connection to google in tls
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #login using your credentials
    server.login('username@gmail.com', 'password')

    subject = f"{title} Price Fell Down!! - Custom Watchlist"
    body = f"Current price is {price}.Check out this link{URL}"

    msg = f"Subject: {subject}\n\n{body}"
    #Use sender and Receiver's mail address. You can use the same address on both
    server.sendmail("sender@gmail.com", "receiver@gmail.com", msg)

    print('Email has been sent')
    # server.quit()


while(True):
    check_price()
    #If you want to do it one time Remove the while part and run check_price() method once
    time.sleep(86400)