from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'Message sent!')
            form = ContactForm()
        else:
            messages.error(request, 'Error!')

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')
