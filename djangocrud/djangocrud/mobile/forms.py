from django import forms  
from mobile.models import Phone  
class MobileForm(forms.ModelForm):  
    class Meta:  
        model = Phone  
        fields = "__all__"  