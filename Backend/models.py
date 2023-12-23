from django.db import models

# Create your models here.

class flightdb(models.Model):
    flightname = models.CharField(max_length=50,null=True,blank=True)
    flightnumber = models.IntegerField(null=True,blank=True)
    pioletname = models.CharField(max_length=50,null=True,blank=True)
    copioletname = models.CharField(max_length=50,null=True,blank=True)

    fromplace = models.CharField(max_length=30,null=True,blank=True)
    toplace = models.CharField(max_length=30,null=True,blank=True)

    totalseat = models.IntegerField(null=True, blank=True)

    economyseat = models.IntegerField(null=True, blank=True)
    busnissseat = models.IntegerField(null=True, blank=True)
    firstclassseat = models.IntegerField(null=True, blank=True)

    economyprice = models.IntegerField(null=True, blank=True)
    busnissprice = models.IntegerField(null=True, blank=True)
    firstclassprice = models.IntegerField(null=True, blank=True)

    description = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to="Flight_image",null=True,blank=True)


class tourpackagedb(models.Model):
    tourname = models.CharField(max_length=25,null=True,blank=True)
    tourprice = models.IntegerField(null=True,blank=True)
    tourduration = models.CharField(max_length=50,null=True,blank=True)
    tourdescription = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(upload_to="TourPackage_image", null=True, blank=True)



class hotelexploredb(models.Model):
    explorename = models.CharField(max_length=100,null=True,blank=True)
    exploredescription = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="explore_image", null=True, blank=True)


class hotelroomcatagorydb(models.Model):
    roomcatagory = models.CharField(max_length=50,null=True,blank=True)
    roomcatdescription = models.CharField(max_length=150,null=True,blank=True)
    image = models.ImageField(upload_to="Hotelcat_image", null=True, blank=True)

class roomdb(models.Model):
    catname = models.CharField(max_length=25,null=True,blank=True)
    roomname = models.CharField(max_length=25,null=True,blank=True)
    roomdescription = models.CharField(max_length=125,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to="room_image",null=True,blank=True)