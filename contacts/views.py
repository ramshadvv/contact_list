from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def contacts(request):
    contact_list = contactlist.objects.all()
    k = 1
    return render(request,'contacts.html', {'contacts' : contact_list})

def create_contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['number']
        item = contactlist.objects.create(name=name, Phone_number=contact)
        item.save()
        return redirect(create_contacts)
    return render(request, 'register.html')

