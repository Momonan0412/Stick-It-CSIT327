from django import forms
from django.contrib.auth.models import User
from authentication.models import UserProfile

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = UserProfile
        fields = ['description']

    # class Meta:
    #     model = UserProfile
    #     fields = ["first_name", "last_name"]
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile.save()
        return profile
    

class SocialLinksEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["facebook_link","linkedin_link","twitter_link"]
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile

    # facebook_link = forms.CharField(max_length=100)
    # linkedin_link = forms.CharField(max_length=100)
    # twitter_link = forms.CharField(max_length=100)