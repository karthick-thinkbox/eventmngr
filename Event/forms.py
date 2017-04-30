from django import forms
from .models import  user_data,event_info
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class userform(ModelForm):
    class Meta:
        model=user_data
        fields=['name','mobile','email','idcard_img','ticket_count','reg_type','Event',]
        
class eventform(ModelForm):
    class Meta:
        model=event_info
        fields=['Event_name','Event_date','Location','Event_type']
        widgets = {
            'Event_date': DateInput()
        }


        
        
        