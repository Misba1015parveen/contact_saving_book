
from django import forms 
from .models import ContactBook
class ContactBookForm(forms.ModelForm):
    
    class Meta:

        model = ContactBook
        fields = ("image", "mobile_number", "email", "label", "person_name")
    def clean(self):
        cleaned_data= super().clean()
        valmobile=self.cleaned_data.get('mobile_number')
        valemail=self.cleaned_data.get('email')
        vallabel=self.cleaned_data.get('label')
        valname=self.cleaned_data.get('person_name')
        if not valmobile.isdigit():
            raise forms.ValidationError('Mobile number should contain only digits.')
        if len(valemail) < 10:
            raise forms.ValidationError('Email should be more than 10.')         
        if len(vallabel) < 3:
            raise forms.ValidationError('Label should be more than 3.') 
        if len(valname) < 4:
            raise forms.ValidationError('Name should be more than 4.')       

       
        
class SearchForm(forms.Form):
    search = forms.CharField( max_length=100, required=False)