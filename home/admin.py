from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Department, Team , Appointment , Message
# Register your models here.

admin.site.register(Department)
admin.site.register(Team)


class MessageTable(admin.ModelAdmin):
   
    list_display = ("id" ,'yor_name' ,'yor_phn', 'your_Email' ,'subjects', 'messsage' , )
    

admin.site.register(Message,MessageTable)



class AppointmentAdmin(admin.ModelAdmin):
   
    list_display = ("id" ,"pet_name" , 'pet_phn' , 'pet_Email' , 'booking_date' , 'doc_name' , 'booked_on' )
    
    

admin.site.register(Appointment,AppointmentAdmin)
