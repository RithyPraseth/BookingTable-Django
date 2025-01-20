from rest_framework import serializers

from .models import *

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblBookTable
        fields = ['custName', 'email', 'phoneNumber', 'bookDate', 'bookTime', 'noPeople', 'description']