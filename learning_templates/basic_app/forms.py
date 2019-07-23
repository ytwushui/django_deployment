from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# add what included in the form, 1 from user 2 from userprofileinf <-- self defineded
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
