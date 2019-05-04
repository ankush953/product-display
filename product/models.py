from django.db import models

class PhoneBrand(models.Model):
    brandName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.brandName

# function to define where images will be stored
def phone_gallery(request,filename):
    return request.brand.__str__() +'/'+request.name+'.jpg'


class Product(models.Model):
    # Attributes of product
    brand = models.ForeignKey(PhoneBrand,on_delete=models.CASCADE)   # Company of product
    name = models.CharField(max_length=100)                          # Name of product
    price = models.DecimalField(max_digits=10, decimal_places=2)     # price of product
    ram = models.IntegerField()                                      # ram of smartphone
    rom = models.IntegerField()                                      # rom of smartphone
    battery = models.IntegerField()                                  # battery capacity of smartphone
    screen = models.DecimalField(max_digits=3,decimal_places=1)      # screen size of phone
    image = models.ImageField(blank=True,upload_to=phone_gallery)    # image of smartphone
    instock = models.IntegerField(default=0)                         # how many products all available


    def __str__(self):
        return self.brand.__str__() + ' ' + self.name

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.product.__str__()
