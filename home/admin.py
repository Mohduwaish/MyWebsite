from django.contrib import admin
from .models import Contact,Slot ,EmailSubscriber,Client, PDFFile

# Register your models here.

admin.site.register(Contact)
admin.site.register(Slot)
admin.site.register(Client)
admin.site.register(EmailSubscriber)
admin.site.register(PDFFile)