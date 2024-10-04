from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
# from django.views.generic import ListView
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
    try:
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact created successfully!')
                return redirect('contact_list')
        else:
            form = ContactForm()
        return render(request, 'contacts/contact_form.html', {'form': form})
    except Exception as e:
        messages.error(request, 'An error occurred while creating the contact.')
        return render(request, 'contacts/contact_form.html', {'form': form})

# Update an existing contact
def contact_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    
    try:
        if request.method == "POST":
            form = ContactForm(request.POST, instance=contact)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact updated successfully!')
                return redirect('contact_list')
            else:
                messages.error(request, 'There was an issue with the form. Please correct the errors and try again.')
        else:
            form = ContactForm(instance=contact)
            
    except Exception as e:
        messages.error(request, 'An unexpected error occurred while updating the contact.')
        return render(request, 'contacts/contact_form.html', {'form': form})
    
    return render(request, 'contacts/contact_form.html', {'form': form})

# Delete a contact
def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        try:
            contact.delete()
            messages.success(request, 'Contact deleted successfully!')
            return redirect('contact_list')
        except Exception as e:
            messages.error(request, 'An error occurred while deleting the contact.')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})