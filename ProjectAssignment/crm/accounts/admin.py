from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Booking Table Restaurant"
admin.site.site_title = "Booking Table Restaurant Admin Panel"
admin.site.index_title = "Booking Table Restaurant Admin Panel"

admin.site.register(Category)
admin.site.register(tblProducts)
admin.site.register(tblTopMenu)
admin.site.register(tblSub2TopMenu)
admin.site.register(tblSubTopMenu)