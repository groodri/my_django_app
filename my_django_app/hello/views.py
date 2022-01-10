from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage

def index(request):
    return render(request, 'index.html')

def sendEmail(request):
    email = request.POST["email"]
    subject = "Something"
    from_email = "From <groodri@outlook.com>"
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
    form = loginuser(request.POST or None)
    message = "Logged in!"
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        iscandidate = Candidate.objects.filter(email.email, password=password).first()
        if iscandidate:
            request.session["id_candidate"] = iscandidate.id
            return redirect("/user")
        else:
            message="Wrong credentials"

    context = {
        "form": form,
        "message": message,
    }
    return render(request, "loginuser.html", context)


def registeruser(request):
    form = registeruser(request.POST or None)
    message = ""
    if request.method == "POST":
        form = register(data=request.POST)

        if form.is_valid():
            address = Response.objects.filter(email=form.cleaned_data["email"])
            if len(address) >= 1:
                candidate = Candidate.objects.filter(email=form.cleaned_data["email"]).first()
                if not candidate:
                    user = form.save()
                    if user is not None:
                        return redirect('/loginuser')
                else:
                    message="registered"
            else:
                message="error"

    return render(request, "registeruser.html", {'form': form, "message": message})

def password(request):
    return render(request, "password.html")