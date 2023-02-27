from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django_quill.forms import QuillFormField
from .models import(
    Ticket,
    Profile
)


class TicketForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = Ticket
        fields = ('title','content')
        
        Widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class SearchForm(forms.Form):
    ALL = "All"

    CHOICES = [
        (ALL, "All")
    ]

    SEARCH_COMPANIES = [] + Profile.COMPANIES
    del SEARCH_COMPANIES[0]
    
    CUSTOM_CHOICES = [(c[0], c[1]) for c in CHOICES]

    company = forms.ChoiceField(choices=CUSTOM_CHOICES + SEARCH_COMPANIES, widget=forms.Select(attrs={'class' : 'form-control'}))
    country = forms.ChoiceField(choices=CUSTOM_CHOICES + Profile.COUNTRY_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))


class UpdateTicketForm(forms.Form):
    content = QuillFormField()
    class Meta:
        model = Ticket
        fiels = ('is_urgent', 'status')

        Widget = {
            'is_urgent' : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'status' : forms.CheckboxInput(attrs={'class': 'form-control'})
        }



