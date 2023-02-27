
import profile
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm, EditSettingsForm
from main.models import Profile, Ticket
from django.views.generic import CreateView, DetailView, UpdateView
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Count


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html",{"form":form})


class EditProfilePageView(generic.UpdateView):
    model =Profile
    template_name = 'registration/edit_profile.html'
    fields = [
        'first_name',
        'last_name',
        'phone_number',
        'company',
        'country',
        ]
    success_url = reverse_lazy('home')

class EditSettingsView(generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'
    ordering = ['-date_added']
    

    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        ticket_list = Ticket.objects.filter(author=page_user.user)
        context["ticket_list"] = ticket_list
        context["page_user"] = page_user
        return context
    
    
    