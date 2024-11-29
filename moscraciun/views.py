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


def become_santa(request, letter_id):
    if request.method == "POST":
        # Get the associated letter
        letter = get_object_or_404(Wishing, id=letter_id)

        # Create the Elf entry
        Elf.objects.create(
            name=request.POST.get("name"),
            phone_number=request.POST.get("phone_number"),
            email=request.POST.get("email"),
            associated_letter=letter,
        )

        # Update the letter status to "APPLIED"
        letter.status = "APPLIED"
        letter.save()

        # Add success message using the messages framework
        messages.success(request, f"Multumesc ca vrei sa faci o fapta buna! "
                                  f"Cererea pentru scrisoarea '{letter.name}' este acum procesata "
                                  f"si revin in scurt timp spre tine.")

        # Redirect back to the wishings list page
        return redirect('home')
    return redirect('home')
