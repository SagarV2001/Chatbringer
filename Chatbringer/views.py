import os

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from methods import *
from user.models import *

error=None

def get_index(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    if main_user:
        return redirect(get_main_page)
    else:
        global alt_text1
        response = render(request, 'index.html', {'alt_text': alt_text1})
        response = clear_cookies(response)
        return response
def get_login(request):
    # User.objects.get(username = 'user_any').delete()
    print(User.objects.all())
    # User.objects.all().delete()
    print(FriendRequest.objects.all())
    global error
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        main_user = authenticated(username,password)
        if main_user:
            response = redirect(get_main_page)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response
        else:
            error = 'Username or Password do not match.'
            return redirect(get_login)
    else:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        main_user = authenticated(username,password)
        if main_user:
            return redirect(get_main_page)
        else:
            response = render(request,'login.html',{'alt_text':alt_text4,'error':error})
            error = None
            response = clear_cookies(response)
            return response
def get_signup(request):
    global error
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        email = request.POST.get('email')
        if not User.objects.filter(Q(email=email) | Q(username=username)).exists():
            if send_otp(request,email):
                response = redirect(get_verification_page)
                response.set_cookie('username',username)
                print(request.COOKIES.get('username'))
                response.set_cookie('password',pwd)
                response.set_cookie('email',email)
                return response
        error = 'Email, Username not valid or already exists.'
    else:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        main_user = authenticated(username,password)
        if main_user:
            return redirect(get_main_page)
    response = render(request,'signup.html',{'alt_text':alt_text3,'error':error})
    error = None
    response = clear_cookies(response)
    return response
def get_main_page(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username,password)
    if main_user:
        friends = main_user.get_friends()
        return render(request,'main.html',context={'user_list':friends})
    else:
        return redirect(get_login)
def get_chat_page(request,other_username):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    if main_user:
        try:
            if main_user.is_friend(other_username):
                other_user = User.objects.get(username=other_username)
                messages = Message.objects.filter(Q(sender=other_user, receiver=main_user) | Q(sender=main_user, receiver=other_user))
                messages = messages.order_by('timestamp')
                res= render(request, 'chat.html', context={'other_user': other_user, 'messages': messages})
                return res
        except Exception as e:
            print(e)
            return redirect(get_main_page)
    return redirect(get_main_page)
def get_verification_page(request):
    if request.method == 'POST':
        request.session['posted-OTP'] = request.POST.get('OTP')
        return redirect(verify_email)
    else:
        global alt_text1
        return render(request,'otpVerification.html',{'alt_text':alt_text1})

def verify_email(request):
    global error
    if request.session.get('posted-OTP') == request.session.get('OTP'):
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        email = request.COOKIES.get('email')
        User.objects.create(
            username=username,
            email=email,
            password=password,
            profile_image='profile-image.jpg'
        )
        request.session.pop('OTP')
        return redirect(get_main_page)
    error = 'Please enter valid otp next time.'
    response = redirect(get_signup)
    response = clear_cookies(response)
    request.session.pop('OTP')
    return response

def logout(request):
    response = redirect(get_index)
    response = clear_cookies(response)
    return response

def search_user(request):
    username = request.COOKIES.get('username')
    curr_user = User.objects.get(username = username)
    search_text = request.GET.get('search-text')
    if search_text is None:
        search_text=''
    found_users = User.objects.filter(username__icontains=search_text)
    friend_list = [friend.username for friend in curr_user.get_friends()]
    request.session['friendlist'] = friend_list
    user_list = [user for user in found_users]
    response = render(request,'searched-users.html',{'username':username,'user_list':user_list,'friend_list':friend_list})
    return response

def send_friend_request(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    if main_user:
        selected_username = request.POST.get('selected-username')
        main_user.send_friend_request(selected_username)
        return redirect(search_user)
    return redirect(get_login)

def get_profile_page(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username,password)
    # debug line
    if main_user:
        return render(request, 'profile.html',{'curr_user':main_user})
    else:
        return redirect(get_login)
def get_friend_requests_page(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    #debug line
    friend_requests = [x.from_user for x in main_user.get_friend_requests()]
    if main_user:
        return render(request, 'friend-requests.html',context={'user_list':friend_requests})
    else:
        return redirect(get_login)

def process_friend_request(request,action):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    if request.method=='POST' and main_user:
        selected_user_name = request.POST.get('selected-username')
        if action=='accept':
            main_user.accept_friend_request(selected_user_name)
        elif action=='reject':
            main_user.reject_friend_request(selected_user_name)
        return redirect(get_friend_requests_page)
    redirect(get_login)
def send_message(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    if request.method == 'POST' and main_user:
        message = request.POST.get('message-text')
        receiver_name = request.POST.get('receiver-name')
        if main_user.is_friend(receiver_name):
            receiver = User.objects.get(username=receiver_name)
            Message.objects.create(sender=main_user,receiver=receiver,content=message)
            print('Message sent.')
            return redirect(f"/chat/{receiver_name}")
        else:
            print("Frontend tempered.")
    return redirect(get_login)
def set_profile_image(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    main_user = authenticated(username, password)
    if request.method == 'POST' and main_user and request.FILES.get('uploaded-image'):
        print('image got')
        image = request.FILES.get('uploaded-image')
        main_user.profile_image = image
        main_user.save()
        print('image uploaded')
        return redirect(get_profile_page)
    return redirect(get_login)