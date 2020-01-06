from django.shortcuts import render
from django.http import HttpResponseRedirect

from WebApp import forms

def Person_View(request):
    form = forms.PersonForm()
    if request.method == 'POST':
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            print("Person Data for Saving in DB...!!")
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.PersonForm()
    return render(request, 'WebApp/Welcome.html', {'form': form})

def Thank_View(request):
    return render(request, 'WebApp/Thanks.html')