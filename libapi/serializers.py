
from rest_framework import serializers
from .models import Borrowed, Books

#serializer class for our custome user model (table)
class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Borrowed
        # fields from our model
        fields = ("id","name","book","borrowed_time","returned_time")
        
class BooksSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    class Meta:
        
        model = Books
        
        fields  = ("id","book_name","author","publisher","status","status_display")

    def get_status_display(self, obj):
        # print(obj.get_status_display())
        name = obj.get_status_display()
        try:
            int_value = int(name)
            status_name = Books.status_choices[int_value]
            print(status_name)
            return status_name[0]
        except ValueError:
            return name