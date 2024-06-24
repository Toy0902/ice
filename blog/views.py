import email

from django.shortcuts import render

from blog.forms import EmailForm


def contact(request):
    form = EmailForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    context = {
        "form": form,
    }
    return render(request,"contact.html",context=context)

def about(request):
    return render(request,"about.html",context={})

def gallery(request):
    return render(request,"gallery.html",context={})

def product(request):
    return render(request,"product.html",context={})

def service(request):
    return render(request,"service.html",context={})
# Create your views here.
def index(request):
    return render(request, "index.html", context={})