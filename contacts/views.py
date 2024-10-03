from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

# List all contacts
def contact_list(request):
    query = request.GET.get('q', '')
    
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone__icontains=query)
        )
    else:
        contacts = Contact.objects.all()
    
    context = {
        'contacts': contacts,
        'query': query,
    }
    
    return render(request, 'contacts/contact_list.html', context)

# Create a new contact
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

# Update an existing contact
def contact_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

# Delete a contact
def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
