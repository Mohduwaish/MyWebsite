from django.db import models
from django.utils import timezone
# Create your models here.

from django.db import models

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13, null=True)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email

class Slot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country_code = models.CharField(null=True,max_length=5)



    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"

class Client(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     phone_number = models.CharField(max_length=20)
     country_code = models.CharField(null=True,max_length=5)
     unique_session_id = models.TextField()

     def __str__(self):
        return f"Session with {self.name}---{self.unique_session_id}" 

class EmailSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email         
    


class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
