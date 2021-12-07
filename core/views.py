from django.shortcuts import render
from .forms import ContactForm, ProductModelForm
from django.contrib import messages
from django.shortcuts import redirect


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
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProductModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Product saved!')
                form = ProductModelForm()
            else:
                messages.error(request, 'Error!')
        else:
            form = ProductModelForm()

        context = {
            'form': form,
        }
        return render(request, 'product.html', context)

    else:
        return redirect('index')
