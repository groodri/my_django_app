from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from hello.forms import *
from hello.models import *

def index(request):
    return render(request, 'index.html')

def sendEmail(request):
    email = request.POST["email"]
    subject = "Something"
    from_email = "From <contact@plantwizardscommunity.com>"
    to = email
    body_message = "<h1 style='color:red'>Welcome to Something!</h1><p>"
    body_message += "<p font-size: 15px'>Let's do something with something on something.</p>"
    body_message += "<p style='font-style: italic; font-size: 12px'>Message sent automatically.</p>"
    mail = EmailMessage(subject, body_message, to=[email])
    mail.content_subtype = "html"
    mail.send_mail(subject, plain_message, from_email, [to], html_message)

    data = {
        "validation": "ok",
        "id_candidate": id_candidate,
        }

    return JsonResponse(data, safe=False)

def loginuser(request):
    form = loginForm(request.POST or None)
    message = "Logged in!"
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        iscandidate = Candidate.objects.filter(email.email, password=password).first()
        if iscandidate:
            request.session["id_candidate"] = iscandidate.id
            return redirect("/user")
        else:
            message = "Wrong credentials"

    context = {
        "form": form,
        "message": message,
    }

    return render(request, "loginuser.html", context)

def registeruser(request):
    form = registerForm(request.POST or None)
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Candidate.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    
    context = {
        "form": form,
    }

    return render(request, "registeruser.html", context)

# def registeruser(request):
#     form = registerForm(request.POST or None)
#     message = "User registered!"
#     if request.method == "POST":
#         form = registerForm(data=request.POST)

#         if form.is_valid():
#             address = Response.objects.filter(email=form.cleaned_data["email"])
#             if len(address) >= 1:
#                 candidate = Candidate.objects.filter(email=form.cleaned_data["email"]).first()
#                 if not candidate:
#                     user = form.save()
#                     if user is not None:
#                         return redirect('registeruser/')
#                 else:
#                     message="User registered!"
#             else:
#                 message="Error: could not register user."

#     context = {
#         "form": form,
#         "message": message,
#     }

#     return render(request, "registeruser.html", context)

def password(request):
    return render(request, "password.html")