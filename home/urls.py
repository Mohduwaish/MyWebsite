"""iCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from home import views
app_name='home'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('available_slots', views.available_slots, name='available_slots'),
    path('slots/book/<int:slot_id>/',views.book_slot, name='book_slot'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('PDF', views.PDF, name='PDF'),
    path('after_email_subs', views.after_email_subs, name='after_email_subs'),
    path('download_pdf/<int:pdf_id>/', views.download_pdf, name='download_pdf'),

]

