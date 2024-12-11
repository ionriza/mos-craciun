from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Wishing, Elf
from django.db.models import Case, When, Value, IntegerField


def home(request):
    # Define custom ordering for statuses
    wishings = Wishing.objects.annotate(
        custom_order=Case(
            When(status="NOT_APPLIED", then=Value(0)),
            When(status="APPLIED", then=Value(1)),
            When(status="CONFIRMED", then=Value(2)),
            output_field=IntegerField(),
        )
    ).order_by("custom_order", "last_name", "first_name")

    not_applied_count = Wishing.objects.filter(status="NOT_APPLIED").count()
    for wishing in wishings:
        wishing.wishing_items_list = wishing.wishing_items.split(
            "\n"
        )

    return render(
        request,
        "home.html",
        {
            "wishings": wishings,
            "not_applied_count": not_applied_count,
        },
    )


def become_santa(request, wishing_id):
    # Fetch the Wishing object
    wishing = get_object_or_404(Wishing, id=wishing_id)

    # Check if an Elf is already assigned to this letter
    if Elf.objects.filter(associated_letter=wishing).exists():
        messages.error(
            request,
            "Din pacate scrisoarea a fost deja atribuita cuiva. Te rog sa te uiti dupa una noua.",
        )
        return redirect(
            "home"
        )  # Redirect to the homepage or the page listing all letters

    # If no Elf is assigned, proceed to create one
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")

        # Create a new Elf and associate it with the Wishing
        elf = Elf.objects.create(
            name=name, phone_number=phone_number, email=email, associated_letter=wishing
        )

        # Update the Wishing status to "APPLIED"
        wishing.status = "APPLIED"
        wishing.save()

        # Success message
        messages.success(
            request, "Felicitări! Ai devenit Moș Crăciun pentru această scrisoare. 🎅"
        )
        return redirect("home")  # Redirect to the homepage or a success page

    # If not a POST request, return to the homepage
    return redirect("home")
