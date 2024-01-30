from random import Random
import smtplib
import os
from user.models import User

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import reverse

from dotenv import load_dotenv
load_dotenv('constants.env')

rand = Random()

def authenticated(username,password):
    try:
        user_ = User.objects.get(username=username)
        if user_.password == password:
            return user_
        else:
            return None
    except Exception:
        print(Exception)
        print("User does not exist")
        return None
def clear_cookies(response):
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response
def send_otp(request,email):
    rand_num = rand.randint(100000,999999)
    request.session['OTP'] = str(rand_num)
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            sender = os.getenv("SENDER_EMAIL")
            sender_pwd = os.getenv("SENDER_PASSWORD")

            connection.starttls()
            connection.login(user=sender, password=sender_pwd)
            connection.sendmail(from_addr=sender, to_addrs=email, msg=f"Subject:OTP for Messenger Verification.\n\n Please enter following OTP for verification: {rand_num}")
            print(rand_num)

            return True
    except Exception as e:
        print("Failed to send email:", e)
        return None


# html codes for conditional pages
alt_text1 = '''<a class='sign-log-button navbar-item'href="/signup">SignUp</a>
               <a class='sign-log-button navbar-item'href="/login">Login</a>'''

alt_text3 = '''<a class='sign-log-button navbar-item'href="/login">Login</a>'''
alt_text4 = '''<a class='sign-log-button navbar-item'href="/signup">SignUp</a>'''
