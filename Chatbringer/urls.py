"""
URL configuration for Chatbringer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Chatbringer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_index),
    path('login/', views.get_login,name='login'),
    path('signup/', views.get_signup,name='signup'),
    path('logout/',views.logout),
    path('verify-email/',views.get_verification_page,name='verify-email'),
    path('verify/',views.verify_email),
    path('main/',views.get_main_page),
    path('chat/<str:other_username>',views.get_chat_page),
    path('send-message/',views.send_message,name='send-message'),
    path('search-user/',views.search_user,name='search-user'),
    path('add-friend/',views.send_friend_request,name='send-friend-request'),
    path('profile-page/',views.get_profile_page),
    path('friend-requests/',views.get_friend_requests_page),
    path('process-friend-request/<str:action>/',views.process_friend_request,name='process-friend-request'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
