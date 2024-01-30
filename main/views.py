from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm


def user_form(request):
    submitted = False
    if request.method == "POST":
       form = UserForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/form?submitted=True')
    else:
       form = UserForm()
    if 'submitted' in request.GET:
           submitted = True
    return render(request, 'main/form.html', {'form' : form, 'submitted' : submitted})
       


def home(request):           
    return render(request, 'main/home.html', {})

