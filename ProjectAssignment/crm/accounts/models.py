from django.db import models

# Create your models here.
class tblTopMenu(models.Model):
    topMenuName = models.CharField(max_length=200, null=True)
    topMenuImage = models.CharField(max_length=200, null=True)

    def str(self):
        return self.topMenuName

class tblSubTopMenu(models.Model):
    subTopMenuName = models.CharField(max_length=200, null=True)
    subTopMenuImage = models.CharField(max_length=200, null=True)
    TopMenuID = models.ForeignKey(tblTopMenu, on_delete=models.CASCADE, null=True)

    def str(self):
        return f'{self.subTopMenuName}'  

class tblSub2TopMenu(models.Model):
    sub2TopMenuName = models.CharField(max_length=200, null=True)
    sub2TopMenuImage = models.CharField(max_length=200, null=True) 
    subTopMenuID = models.ForeignKey(tblSubTopMenu, on_delete=models.CASCADE, null=True)

    def str(self):
        return f'{self.sub2TopMenuName}'

class Category(models.Model):   
    CategoryName = models.CharField(max_length=200, null=True) 
    CategoryImage =  models.ImageField(upload_to ='CategoryImages/')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.CategoryName 

class tblFoodMenu(models.Model):
    foodName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    foodImage =  models.ImageField(upload_to ='FoodMenuImages/')
    foodDate = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True)
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