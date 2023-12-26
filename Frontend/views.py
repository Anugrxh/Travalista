import razorpay
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Backend.models import flightdb, tourpackagedb, hotelexploredb, hotelroomcatagorydb, roomdb

from Frontend.models import Ratingdb, userdb, contactdb, checkoutflightdb, TourReplydb, roombookeddb
from django.contrib import messages
from django.core.mail import send_mail

from django.core.mail import EmailMessage

# Create your views here.
# LOGIN AND SIGNN UP

def login_frontend(request):
    return render(request,"loginsignup.html")

def usrdata(request):
    if request.method=="POST":
        una=request.POST.get('username')
        ema=request.POST.get('email')
        mob=request.POST.get('mobile')
        pas=request.POST.get('password')
        obj=userdb(username=una,email=ema,mobile=mob,password=pas)
        obj.save()
        messages.success(request,"Account Created...!")

        subject = "Welcome to Travalista"
        message = "Hello" +obj.username + "!!\nWelcome to Travalista \n Thank you for considering us"
        from_email = settings.EMAIL_HOST_USER
        to_list = [obj.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return redirect(login_frontend)

def Userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if userdb.objects.filter(username=un,password=pwd).exists():
            request.session['username']= un
            request.session['password']= pwd
            messages.success(request,"Login success..")
            return redirect(home)
        else:
            messages.error(request,"Invalid username or password..!")
            return redirect(login_frontend)
    else:
        return redirect(login_frontend)

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"User Logged out...!")
    return redirect(login_frontend)


# Home page

def home(request):
    tourdata = tourpackagedb.objects.all()
    rating = Ratingdb.objects.all()
    random = roomdb.objects.order_by('?')[:4]
    return render(request,"home.html",{'tourdata':tourdata,'rating':rating,'random':random})


#ABOUT PAGE

def about(request):
    return render(request,"About.html")

#BOOK NOW


def book_now(request):
    data = flightdb.objects.all()


    return render(request,"BookNow.html",{'data':data})


def book_single(request,pro_id):
    data = flightdb.objects.get(id=pro_id)
    return render(request,"book_single.html",{'data':data})






def booksingledata(request):
    if request.method == "POST":
        frpla = request.POST.get('fromplace')
        topla = request.POST.get('toplace')
        dfr = request.POST.get('datefrom')
        dto = request.POST.get('dateto')
        trcl = request.POST.get('travelclass')
        npasen = request.POST.get('numpassengers')
        epri = request.POST.get('economyprice')

        fna = request.POST.get('fullname')
        gen = request.POST.get('gender')
        mob = request.POST.get('mobile')
        ema = request.POST.get('email')
        pls = request.POST.get('place')
        adar = request.POST.get('aadhar')
        pin = request.POST.get('pincode')
        addr = request.POST.get('address')
        flno = request.POST.get('flightnumber')
        ttpri = request.POST.get('totalticketprice')
        flnam = request.POST.get('flightname')
        piona = request.POST.get('pioletname')
        copiona = request.POST.get('copioletname')
        descr = request.POST.get('description')
        tseat = request.POST.get('totalseat')
        unaa = request.POST.get('username')
        obj=checkoutflightdb(fromplace=frpla,toplace=topla,datefrom=dfr,dateto=dto,travelclass=trcl,numpassengers=npasen,economyprice=epri, fullname=fna,gender=gen,mobile=mob,email=ema,place=pls,aadhar=adar,pincode=pin,address=addr,flightnumber=flno,totalticketprice=ttpri,flightname=flnam,pioletname=piona,copioletname=copiona,description=descr,totalseat=tseat,username=unaa)
        obj.save()
        messages.success(request,"Redirecting to payment page")
        return redirect(payment)


# CONTACT US PAGE
def contact_us(request):
    return render(request,"ContactUs.html")

def contactdata(request):
    if request.method=="POST":
        na=request.POST.get('name')
        una=request.POST.get('username')
        ema=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        obj=contactdb(name=na,username=una,email=ema,subject=sub,message=msg)
        obj.save()
        messages.success(request,"Send succesfully..!")
        return redirect(contact_us)


def bookingcart(request):
    data = checkoutflightdb.objects.filter(username=request.session['username'])
    hoteldata = roombookeddb.objects.filter(username=request.session['username'])
    return render(request,"BookingCart.html",{'data':data,'hoteldata':hoteldata})

def bookinghotel_delete(request,pro_id):
    pro = roombookeddb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request,"Booking canceled,You will not get compleate refund.")
    return redirect(bookingcart)

def bookingcart_delete(request,pro_id):
    pro = checkoutflightdb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request,"Booking canceled,You will not get compleate refund.")
    return redirect(bookingcart)





# def payment(request):
#     if request.method=="POST":
#         amount=50000
#         order_currency='INR'
#         client = razorpay.Client(auth=('rzp_test_jcVIUHkalKhqwa','Gwt5sgqFhjy0ur0qJUKQxTwY'))
#         payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
#     return render(request,"payment.html")



def payment(request):
    last_object = checkoutflightdb.objects.order_by('-id').first()
    payy = last_object.totalticketprice
    payy_str = str(payy)
    for ptotl in payy_str:
        print(ptotl)



    if request.method=="POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_jcVIUHkalKhqwa','Gwt5sgqFhjy0ur0qJUKQxTwY'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"payment.html",{'payy_str':payy_str})


def RatingPage(request):
    return render(request,"RatingPage.html")



def Ratingdata(request):
    if request.method == "POST":
        una = request.POST.get('username')
        ema = request.POST.get('email')
        des = request.POST.get('description')
        rat = request.POST.get('rating')
        obj = Ratingdb(username=una,email=ema,description=des,rating=rat)
        obj.save()
        messages.success(request,"Thank you for using travalista")
        return redirect(home)
    else:
        # Handle the non-POST case
        return HttpResponse('This view only accepts POST requests.')



def TourSingle(request,tourid):
    tourdata = tourpackagedb.objects.get(id=tourid)
    return render(request,"TourSingle.html",{'tourdata':tourdata})

def TourReplyData(request):
    if request.method =="POST":
        tema = request.POST.get('touremail')
        tpla = request.POST.get('tourplace')
        una = request.POST.get('username')
        tmsg = request.POST.get('tourmessage')
        tpri = request.POST.get('tourprice')
        obj = TourReplydb(touremail=tema,tourplace=tpla,username=una,tourmessage=tmsg,tourprice=tpri)
        obj.save()
        messages.success(request,"Send Succesfully...Our team will contact you shortly ")
        return redirect(home)



# HOTELL INDEX


def hotelindex(request):
    exp = hotelexploredb.objects.all()
    cat = hotelroomcatagorydb.objects.all()
    random = roomdb.objects.order_by('?')[:4]  # change 5 to the number of records you want

    rating = Ratingdb.objects.all()
    return render(request,"HotelIndex.html",{'exp':exp,'cat':cat,'rating':rating,'random':random})

def roomslist(request,room_name):
    rooms = roomdb.objects.filter(catname=room_name)
    return render(request,"HotelBookNow.html",{'rooms':rooms})

def room_single(request,room_id):
    data = roomdb.objects.get(id=room_id)
    return render(request,"HotelRoomSingle.html",{'data':data})


from Frontend.models import roombookeddb
from django.conf import settings
from Travalista import settings

def roombookeddata(request):
    if request.method == "POST":
        hcn = request.POST.get('hotelcustomername')
        una = request.POST.get('username')
        rmna = request.POST.get('roomname')
        hcem = request.POST.get('hotelcustomeremail')
        hcmo = request.POST.get('hotelcustomermobile')
        hbsd = request.POST.get('hotelbookingstartdate')
        hbed = request.POST.get('hotelbookingenddate')
        hpri = request.POST.get('hotelprice')
        obj = roombookeddb(hotelcustomername=hcn,username=una,roomname=rmna,hotelcustomeremail=hcem,hotelcustomermobile=hcmo,hotelbookingstartdate=hbsd,hotelbookingenddate=hbed,hotelprice=hpri)
        obj.save()

        return redirect(payment_hotel)

def payment_hotel(request):

    last_object = roombookeddb.objects.order_by('-id').first()
    payy = last_object.hotelprice
    payy_str_hotel = str(payy)
    for ptotl in payy_str_hotel:
        print(ptotl)

    if request.method == "POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_jcVIUHkalKhqwa','Gwt5sgqFhjy0ur0qJUKQxTwY'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"payment_hotel.html",{'payy_str_hotel':payy_str_hotel})


