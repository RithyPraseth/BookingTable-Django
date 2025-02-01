from django.db import models

# Create your models here.
class tblContactUs(models.Model):
    address = models.CharField(max_length=200, null=True)
    callUs = models.CharField(max_length=200, null=True)
    emailUs = models.CharField(max_length=200, null=True)
    openHour = models.CharField(max_length=200, null=True)
    def __str__(self):         
        return self.address  
    
class tblwhyUs(models.Model):
    icon = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):         
        return self.title  




class tblTopMenu(models.Model):
    topMenuName = models.CharField(max_length=200, null=True)
    topMenuImage = models.CharField(max_length=200, null=True)
    topMenuLink = models.CharField(max_length=200)

    def __str__(self):
        return self.topMenuName

class Category(models.Model):   
    CategoryName = models.CharField(max_length=200, null=True) 
    CategoryImage =  models.ImageField(upload_to ='CategoryImages/')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.CategoryName 

class tblFoodMenu(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'   
    
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    foodName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    foodImage = models.ImageField(upload_to='FoodMenuImages/')
    foodDate = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return self.foodName

    
class tblAboutUs(models.Model):
    aboutUsName = models.CharField(max_length=200, null=True)
    aboutUsImage = models.ImageField(upload_to ='AboutUsImages/')
    videoImage = models.ImageField(upload_to ='AboutUsImages/')
    phoneNumber = models.CharField(max_length=15, null=True)
    advan1 = models.CharField(max_length=200, null=True)
    advan2 = models.CharField(max_length=200, null=True)
    advan3 = models.CharField(max_length=200, null=True)
    advan4 = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    aboutDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return self.aboutUsName  


class tblEnventCatalog(models.Model):
    catalogName = models.CharField(max_length=200, null=True)
    catalogPrice = models.CharField(max_length=200, null=True)
    catalogImage = models.ImageField(upload_to ='CatalogImages/')
    phoneNumber = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=200, null=True)
    catalogDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return self.catalogName  
    
class tblBookTable(models.Model):
    custName = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=15, null=True)
    bookDate = models.DateField(null=True)
    bookTime = models.TimeField(null=True)
    noPeople = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):         
        return self.custName

class tblSlide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slideImage = models.ImageField(upload_to ='SlideImages/')
    video_url = models.URLField(null=True, blank=True)
    button_text = models.CharField(max_length=100, default='Book a Table', editable=False)
    button_link = models.CharField(max_length=200, default='#book-a-table', editable=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class tblChef(models.Model):
    chefName = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    chefDescription = models.CharField(max_length=200, null=True)
    chefImage = models.ImageField(upload_to ='ChefImages/')
    def __str__(self):         
        return self.chefName

class tblGallery(models.Model):
    ImageName = models.CharField(max_length=200, null=True)
    Image = models.ImageField(upload_to ='GalleryImages/')
    def __str__(self):         
        return self.ImageName