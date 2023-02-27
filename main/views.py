from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Ticket, Profile
from django.contrib.auth.models import User
from .forms import TicketForm, SearchForm
from django.db.models import Q

class HomeView(ListView):
    model = Ticket
    template_name = 'main/home.html'
    context_object_name = 'tickets'
    ordering = ['-date_added']
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)

        if 'company' in self.request.GET:
            company = self.request.GET.get('company')
            if company != 'SUP':
                context['tickets'] = Ticket.objects.filter(company=company)
        
        if 'country' in self.request.GET:
            country = self.request.GET.get('country')
            if country != 'All':
                context['tickets'] = Ticket.objects.filter(country=country)

        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            company = form.cleaned_data['company']
            country = form.cleaned_data['country']
            if company == 'All' and country == "All":
                return queryset
            elif company == "All":
                return queryset.filter(country=country)
            elif country == 'All':
                return queryset.filter(company=company)
            return queryset.filter(company=company, country=country)
        return queryset
    

class AddTicketView(CreateView):
    model =Ticket
    form_class = TicketForm
    template_name = 'main/add_ticket.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')


class TicketDetailView(DetailView):
    model = Ticket
    template_name = "main/ticket_detail.html"

    def get_context_data(self, **kwargs):
        # ticket = self.get_object()
        context = super().get_context_data(**kwargs)
        return context
    
class UpdateTicketView(UpdateView):
    model = Ticket
    template_name = "main/ticket_detail.html"
    

    

