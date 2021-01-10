import smtplib
import requests
import hyperlink
import re
from email.message import EmailMessage
from Amazon_Scraper import AmazonScraper

def isValidEmail(email)->bool:
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    return (not match==None)

def getEmail()->str:
    email = str(input("What is your email: "))
    while(not isValidEmail(email)):
        email = str(input("Please enter a valid email: "))
    return email

if __name__ == '__main__':
    email = getEmail()
    #number = getNumber()+"@pm.sprint.com"
    #print(url_String)
    scraper = AmazonScraper()
    print("This worked")
    scraper.searchProductList(email)
