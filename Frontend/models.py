from django.db import models

# Create your models here.
class userdb(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)


class contactdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    subject=models.CharField(max_length=50,null=True,blank=True)
    message=models.CharField(max_length=50,null=True,blank=True)


class checkoutflightdb(models.Model):

    fromplace = models.CharField(max_length=50,null=True,blank=True)
    toplace = models.CharField(max_length=50,null=True,blank=True)
    datefrom = models.CharField(max_length=20,null=True,blank=True)
    dateto = models.CharField(max_length=20,null=True,blank=True)
    travelclass = models.CharField(max_length=50,null=True,blank=True)
    numpassengers = models.IntegerField(null=True, blank=True)
    economyprice = models.IntegerField(null=True, blank=True)

    fullname = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    aadhar = models.IntegerField(null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    flightnumber = models.IntegerField(null=True, blank=True)
    totalticketprice = models.IntegerField(null=True, blank=True)
    flightname = models.CharField(max_length=50,null=True,blank=True)
    pioletname = models.CharField(max_length=50,null=True,blank=True)
    copioletname = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    totalseat = models.IntegerField(null=True, blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)


class Ratingdb(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    rating=models.IntegerField()



class TourReplydb(models.Model):
    touremail = models.CharField(max_length=20,null=True,blank=True)
    tourplace = models.CharField(max_length=20,null=True,blank=True)
    username = models.CharField(max_length=20,null=True,blank=True)
    tourmessage = models.CharField(max_length=20,null=True,blank=True)
    tourprice = models.IntegerField(null=True,blank=True)

class roombookeddb(models.Model):
    hotelcustomername = models.CharField(max_length=30,null=True,blank=True)
    username = models.CharField(max_length=30,null=True,blank=True)
    roomname = models.CharField(max_length=30,null=True,blank=True)
    hotelcustomeremail = models.CharField(max_length=30,null=True,blank=True)
    hotelcustomermobile = models.IntegerField(null=True,blank=True)
    hotelbookingstartdate = models.CharField(max_length=30,null=True,blank=True)
    hotelbookingenddate = models.CharField(max_length=30,null=True,blank=True)
    hotelprice = models.IntegerField(null=True,blank=True)
