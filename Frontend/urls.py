from django.urls import path
from Frontend import views
from django.contrib import admin
urlpatterns = [
   path('home/',views.home,name="home"),
   path('about/',views.about,name="about"),
   path('contact_us/',views.contact_us,name="contact_us"),
   path('book_now/',views.book_now,name="book_now"),
   path('book_single/<int:pro_id>/',views.book_single,name="book_single"),
   path('payment/', views.payment, name="payment"),
   path('bookingcart/', views.bookingcart, name="bookingcart"),
   path('bookingcart_delete/<int:pro_id>/', views.bookingcart_delete, name="bookingcart_delete"),
   path('bookinghotel_delete/<int:pro_id>/', views.bookinghotel_delete, name="bookinghotel_delete"),


   path('login_frontend/',views.login_frontend,name="login_frontend"),
   path('usrdata/',views.usrdata,name="usrdata"),
   path('Userlogin/',views.Userlogin,name="Userlogin"),
   path('Userlogout/',views.Userlogout,name="Userlogout"),


   path('contactdata/',views.contactdata,name="contactdata"),
   path('booksingledata/',views.booksingledata,name="booksingledata"),
   path('RatingPage/',views.RatingPage,name="RatingPage"),
   path('TourSingle/<int:tourid>/',views.TourSingle,name="TourSingle"),
   path('Ratingdata/',views.Ratingdata,name="Ratingdata"),
   path('TourReplyData/',views.TourReplyData,name="TourReplyData"),


   path('hotelindex/',views.hotelindex,name="hotelindex"),
   path('payment_hotel/',views.payment_hotel,name="payment_hotel"),
   path('room_single/<int:room_id>/',views.room_single,name="room_single"),
   path('roombookeddata/',views.roombookeddata,name="roombookeddata"),
   path('roomslist/<room_name>/',views.roomslist,name="roomslist"),


   # path('paymentrating/',views.paymentrating,name="paymentrating"),







]