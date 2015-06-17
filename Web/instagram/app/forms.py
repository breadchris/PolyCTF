from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from app.models import InstagramUser

class InstagramUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=255)
    username = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    password_check = forms.CharField(max_length=255, label="Re-enter password")
    profile_picture = forms.ImageField()
    
    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_check')
        
        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data

    class Meta:
        fields = ('name', 'email', 'username', 'password', 'password_check')
        model = InstagramUser

