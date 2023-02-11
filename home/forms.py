from django import forms

from. models import Appointment , Message

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields= '__all__'


        widgets = {
            'booking_date': DateInput(),
        }

        labels={

            'pet_name'    : 'Patient Name',
            'pet_phn'     : 'patient Phone', 
            'pet_Email'   : 'patient Email',
            'booking_date': 'Booking Date',
            'doc_name'    : 'Doctor Name'
          

        }

class messagform(forms.ModelForm):
    class Meta:
        model=Message
        fields='__all__'


     



   