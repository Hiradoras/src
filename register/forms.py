from dataclasses import fields
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from main.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    company = forms.ChoiceField(choices=Profile.COMPANY_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))
    country = forms.ChoiceField(choices=Profile.COUNTRY_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'company',
            'country',
            'password1',
            'password2'
        ]

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            phone_number=instance.profile.phone_number if hasattr(instance, 'profile') else '',
            company=instance.profile.company  if hasattr(instance, 'profile') else '',
            country=instance.profile.country  if hasattr(instance, 'profile') else '',
        )
        if hasattr(instance, 'profile'):
            profile = Profile.objects.get(user=instance)
            profile.phone_number = instance.profile.phone_number
            profile.save()


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    company = forms.ChoiceField(choices=Profile.COMPANY_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))
    country = forms.ChoiceField(choices=Profile.COUNTRY_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))
    

    class Meta:
        model = User
        fields = ('email', 'first_name','last_name','username', 'phone_number', 'company', 'country')