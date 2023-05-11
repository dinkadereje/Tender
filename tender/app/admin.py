from django.contrib import admin
from .models import Category,Tender,Region,Company,DocumentBid
# Register your models here.
admin.site.register(Category)
admin.site.register(Tender)
admin.site.register(Region)
admin.site.register(Company)
admin.site.register(DocumentBid)