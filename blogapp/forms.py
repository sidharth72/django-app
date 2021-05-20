from .models import Profile,Post,Comment
from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from django.forms import ModelChoiceField
from django.forms.models import inlineformset_factory




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

        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Your email'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Your comment..'})
        }


#class PostForm(forms.ModelForm):
 #   profile_data = forms.ModelChoiceField(queryset=Profile.objects.all())
  #  class Meta:
   #     model = Post
    #    fields = ['title','blog']
     #   widgets = {

      #      'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Title..'})
       # }

#ProfilePostForm = inlineformset_factory(Post,Profile,fields=('post'))





