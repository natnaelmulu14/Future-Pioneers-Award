from django import forms
from django.forms import ModelForm
from .models import calcData

class dataInputForm(forms.ModelForm):
    class Meta:
        model = calcData  # This specifies the model that the form is based on
        fields = "__all__"  # This includes all fields from the model in the form
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'Enter value',"class":"form-group"}),  # Replace 'your_field_name' with actual field name
            # Add more fields here if needed
        }

