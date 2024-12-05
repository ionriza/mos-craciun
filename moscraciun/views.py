from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Wishing, Elf


def home(request):
    wishings = Wishing.objects.all()  # Fetch all wishings
    not_applied_count = Wishing.objects.filter(status='NOT_APPLIED').count()
    for wishing in wishings:
        wishing.wishing_items_list = wishing.wishing_items.split("\n")  # Preprocess the list
    return render(request, 'home.html', {
        'wishings': wishings,
        'not_applied_count': not_applied_count,
    })


def become_santa(request, wishing_id):
    # Fetch the Wishing object
    wishing = get_object_or_404(Wishing, id=wishing_id)

    # Check if an Elf is already assigned to this letter
    if Elf.objects.filter(associated_letter=wishing).exists():
        messages.error(
            request,
            "Din pacate scrisoarea a fost deja atribuita cuiva. Te rog sa te uiti dupa una noua."
        )
        return redirect('home')  # Redirect to the homepage or the page listing all letters

    # If no Elf is assigned, proceed to create one
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        # Create a new Elf and associate it with the Wishing
        elf = Elf.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            associated_letter=wishing
        )

        # Update the Wishing status to "APPLIED"
        wishing.status = 'APPLIED'
        wishing.save()

        # Success message
        messages.success(request, "Felicitări! Ai devenit Moș Crăciun pentru această scrisoare. 🎅")
        return redirect('home')  # Redirect to the homepage or a success page

    # If not a POST request, return to the homepage
    return redirect('home')