from django.db import models

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=300,blank=False,null=False)
    author = models.CharField(max_length=300,blank=False,null=False)
    publisher = models.CharField(max_length=300,blank=False,null=False)
    status_choices = (
        ("Available","Available"),
        ("Not Available", "Not Available")
    )
    status = models.CharField(max_length=300,blank=False,null=False,choices=status_choices,default=[0][0])

    def __str__(self):
        return self.book_name
    

class Borrowed(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    borrowed_time = models.DateTimeField(auto_now_add=True)
    returned_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + " borrowed " + self.book.book_name
    
    