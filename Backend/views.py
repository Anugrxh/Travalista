from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

from Backend.models import flightdb, tourpackagedb, hotelexploredb, hotelroomcatagorydb, roomdb
from Frontend.models import contactdb, TourReplydb


# Create your views here.

#Index PAge
def Index_page(request):
    return render(request,"Index.html")


#admin
def Login_admin(request):
    return render(request,"Login.html")

def adminuser(request):
    if request.method == "POST":
        una = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if User.objects.filter(username__contains=una).exists():
            x = authenticate(username=una,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] = una
                request.session['password'] = pwd
                messages.success(request,"Login Successful")
                return redirect(Index_page)
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect(Login_admin)
        else:
            return redirect(Login_admin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Login_admin)


#FLIGHT DATA

def Add_Flight(request):
    return render(request,"AddFlights.html")

def flightdata(request):
    if request.method == "POST":
        flna = request.POST.get('flightname')
        fno = request.POST.get('flightnumber')
        piona = request.POST.get('pioletname')
        cpiona = request.POST.get('copioletname')

        frpla = request.POST.get('fromplace')
        topla = request.POST.get('toplace')

        tsts = request.POST.get('totalseat')
        ests = request.POST.get('economyseat')
        bsts = request.POST.get('busnissseat')
        fcsts = request.POST.get('firstclassseat')

        epri = request.POST.get('economyprice')
        bpri = request.POST.get('busnissprice')
        fcpri = request.POST.get('firstclassprice')

        des = request.POST.get('description')
        img = request.FILES['image']

        obj = flightdb(flightname=flna,flightnumber=fno,pioletname=piona,copioletname=cpiona,fromplace=frpla,toplace=topla,totalseat=tsts,economyseat=ests,busnissseat=bsts,firstclassseat=fcsts,economyprice=epri,busnissprice=bpri,firstclassprice=fcpri,description=des,image=img)
        obj.save()
        messages.success(request,"Flight Details added...!")
        return redirect(Add_Flight)


def Display_Flight(request):
    flightdata = flightdb.objects.all()
    return render(request,"DisplayFlight.html",{'flightdata':flightdata})

def Delete_Flight(request,data_id):
    data = flightdb.objects.filter(id=data_id)
    data.delete()
    messages.error(request,"Deleted Successsfully")
    return redirect(Display_Flight)

def Edit_Flight(request,dataid):
    flight = flightdb.objects.get(id=dataid)
    return render(request,"EditFlight.html",{'flight':flight})


def Update_Flight(request,dataid):
    if request.method == "POST":

        flna = request.POST.get('flightname')
        fno = request.POST.get('flightnumber')
        piona = request.POST.get('pioletname')
        cpiona = request.POST.get('copioletname')

        tsts = request.POST.get('totalseat')
        ests = request.POST.get('economyseat')
        bsts = request.POST.get('busnissseat')
        fcsts = request.POST.get('firstclassseat')

        epri = request.POST.get('economyprice')
        bpri = request.POST.get('busnissprice')
        fcpri = request.POST.get('firstclassprice')

        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = flightdb.objects.get(id=dataid).image
        flightdb.objects.filter(id=dataid).update(flightname=flna,flightnumber=fno,pioletname=piona,copioletname=cpiona,totalseat=tsts,economyseat=ests,busnissseat=bsts,firstclassseat=fcsts,economyprice=epri,busnissprice=bpri,firstclassprice=fcpri,description=des, image=file)
        messages.success(request,"Edited Successfully")
        return redirect(Display_Flight)


# TOUR PACKAGE
def TourPackageAdd(request):
    return render(request,"TourPackageAdd.html")

def tourpackagedata(request):
    if request.method == "POST":
        tna = request.POST.get('tourname')
        tpri = request.POST.get('tourprice')
        tdur = request.POST.get('tourduration')
        tdes = request.POST.get('tourdescription')
        img = request.FILES['image']
        obj = tourpackagedb(tourname=tna,tourprice=tpri,tourduration=tdur,tourdescription=tdes,image=img)
        obj.save()
        messages.success(request, " Details added...!")
        return redirect(TourPackageAdd)



def TourPackageDisplay(request):
    pack = tourpackagedb.objects.all()
    return render(request,"TourPackageDisplay.html",{'pack':pack})

def TourPackageDelete(request,data_id):
    data = tourpackagedb.objects.get(id=data_id)
    data.delete()
    messages.success(request, "Deleted...!")
    return redirect(TourPackageDisplay)


def TourPackageEdit(request,tour_id):
    tour= tourpackagedb.objects.get(id=tour_id)
    return render(request,"TourPackageEdit.html",{'tour':tour})


def TourPackageUpadate(request,tour_id):
    if request.method == "POST":
        tna = request.POST.get('tourname')
        tpri = request.POST.get('tourprice')
        tdur = request.POST.get('tourduration')
        tdes = request.POST.get('tourdescription')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = tourpackagedb.objects.get(id=tour_id).image
        tourpackagedb.objects.filter(id=tour_id).update(tourname=tna,tourprice=tpri,tourduration=tdur,tourdescription=tdes,image=file)
        messages.success(request,"Edited Successfully")
        return redirect(TourPackageDisplay)


def TourPackageReply(request):
    reply = TourReplydb.objects.all()
    return render(request,"TourPackageReply.html",{'reply':reply})

def TourPackageReplyDelete(request,data_id):
    data = TourReplydb.objects.get(id=data_id)
    data.delete()
    messages.success(request, "Deleted...!")
    return redirect(TourPackageReply)


# FRONT END CONTACT US DATA DISPLAY AT ADMIN

def contactusdisplay(request):
    contactdata = contactdb.objects.all()
    return render(request,"ConatctUsDisplay.html",{'contactdata':contactdata})

def contactusdelete(request,data_id):
    data = contactdb.objects.get(id=data_id)
    data.delete()
    messages.success(request, "Deleted...!")
    return redirect(contactusdisplay)


#HOTEL

def explore_hotel(request):
    return render(request,"ExploreHotel.html")

def exploredata(request):
    if request.method == "POST":
        exna = request.POST.get('explorename')
        exdes = request.POST.get('exploredescription')
        img = request.FILES['image']
        obj = hotelexploredb(explorename=exna,exploredescription=exdes,image=img)
        obj.save()
        messages.success(request,"Saved")
        return redirect(explore_hotel)


def expolre_display(request):

    explore = hotelexploredb.objects.all()
    return render(request,"Explore_Display.html",{'explore':explore})

def explore_delete(request,exp_id):
    data = hotelexploredb.objects.get(id=exp_id)
    data.delete()
    messages.success(request,"Deleted Successfully...!")
    return redirect(expolre_display)

def explore_edit(request,exp_id):

    exp = hotelexploredb.objects.get(id=exp_id)
    return render(request,"Explore_Edit.html",{'exp':exp})

def explore_update(request,explo_id):
    if request.method == "POST":
        exna = request.POST.get('explorename')
        exdes = request.POST.get('exploredescription')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = hotelexploredb.objects.get(id=explo_id)
        hotelexploredb.objects.filter(id=explo_id).update(explorename=exna,exploredescription=exdes,image=file)
        return redirect(expolre_display)

def HotelRoomCatagory(request):
    return render(request,"HotelRoomCatagory.html")

def hotel_room_cat(request):
    if request.method=="POST":
        catna = request.POST.get('roomcatagory')
        catdes = request.POST.get('roomcatdescription')
        img = request.FILES['image']
        obj = hotelroomcatagorydb(roomcatagory=catna,roomcatdescription=catdes,image=img)
        obj.save()
        messages.success(request,"Added Successsfully..!!")
        return redirect(HotelRoomCatagory)

def Hotel_RoomCat_Display(request):
    roomcat = hotelroomcatagorydb.objects.all()
    return render(request,"Hotel_RoomCat_Display.html",{'roomcat':roomcat})

def delete_roomCat(request,del_id):
    data = hotelroomcatagorydb.objects.get(id=del_id)
    data.delete()
    messages.success(request,"Deleted Succesfully..!!")
    return redirect(Hotel_RoomCat_Display)

def edit_roomCat(request,cat_id):
    cat = hotelroomcatagorydb.objects.get(id=cat_id)
    return render(request,"Hotel_RoomCat_Edit.html",{'cat':cat})

def Update_RoomCat(request,Cat_id):
    if request.method == "POST":
        catna = request.POST.get('roomcatagory')
        catdes = request.POST.get('roomcatdescription')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = hotelroomcatagorydb.objects.get(id=Cat_id)
        hotelroomcatagorydb.objects.filter(id=Cat_id).update(roomcatagory=catna,roomcatdescription=catdes,image=file)
        return redirect(Hotel_RoomCat_Display)


def hotel_room_add(request):
    cat = hotelroomcatagorydb.objects.all()
    return render(request,"Hotel_RoomsAdd.html",{'cat':cat})

def roomdata(request):
    if request.method == "POST":
        catna = request.POST.get('catname')
        rona = request.POST.get('roomname')
        rodes = request.POST.get('roomdescription')
        pri = request.POST.get('price')
        img = request.FILES['image']
        obj = roomdb(catname=catna,roomname=rona,roomdescription=rodes,price=pri,image=img)
        obj.save()
        messages.success(request,"Room added")
        return redirect(hotel_room_add)


def room_display(request):
    room = roomdb.objects.all()
    return render(request,"Room_Display.html",{'room':room})

def room_edit(request,pro_id):
    cat = hotelroomcatagorydb.objects.all()
    product_room = roomdb.objects.get(id=pro_id)
    return render(request,"Room_Edit.html",{'product_room':product_room, 'cat':cat})

def room_delete(request,del_id):
    data = roomdb.objects.get(id=del_id)
    data.delete()
    messages.success(request,"Deleted succesfully..!")
    return redirect(room_display)
def Update_Room(request,pro_id):
    if request.method == "POST":
        catna = request.POST.get('catname')
        rona = request.POST.get('roomname')
        rodes = request.POST.get('roomdescription')
        pri = request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = roomdb.objects.get(id=pro_id)
        roomdb.objects.filter(id=pro_id).update(catname=catna,roomname=rona,roomdescription=rodes,price=pri,image=file)
        return redirect(room_display)