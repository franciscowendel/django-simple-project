from django.shortcuts import render
from .forms import ContactForm, ProductModelForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Product
from django_simple_project.core.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets


def index(request):
    context = {
        'products': Product.objects.all() # noqa
    }
    return render(request, 'index.html', context)


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
        return render(request, 'product_registration.html', context)

    else:
        return redirect('index')


# APIView
class ProductAPIView(APIView):
    def get(self, request):  # noqa
        products = Product.objects.all()  # noqa
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):  # noqa
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Generics APIView
class ProductsGenericsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()  # noqa
    serializer_class = ProductSerializer


class ProductGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # noqa
    serializer_class = ProductSerializer


# VIEWSETS
class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # noqa
    serializer_class = ProductSerializer
