import yagmail
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import TeamMember, Partner

def home(request):
    """
    Returns the home route
    """
    return render(request, "base/home.html")

def about(request):
    """
    Handles the websites about page
    """
    return render(request, "base/about.html")

def team(request):
    """
    Handles the logic and rendering for displaying our current team
    """
    context = {"members": TeamMember.objects.all()}

    return render(request, "base/team.html", context)

def partners(request):
    """
    Handles our partner page depsite having none rn lmao
    """
    context = {
        'partners': Partner.objects.all()
    }
    p = Partner.objects.all().first()

    return render(request, "base/partners.html", context)

def contact(request):
    """
    Handles the logic for sending / receiving emails here
    """
    if request.method == "POST":
        form = request.POST.copy()

        receiver = "apexteamfossil@gmail.com"
        subject = form.get('subject')
        body = f"Message from: {form.get('email')}\nMessage Follows:\n{form.get('message')}"

        yag = yagmail.SMTP("Setup mail host in here")
        yag.send(
            to=receiver,
            subject=subject,
            contents=body,
        )

        #messages.success(request, "Your query has been sent off to our team.")
        return redirect("base-home")

    return render(request, "base/contact.html")
