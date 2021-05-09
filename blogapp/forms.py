from .models import Profile,Post
from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ['profile_img'] 




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','blog']
        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Title..'})
        }

