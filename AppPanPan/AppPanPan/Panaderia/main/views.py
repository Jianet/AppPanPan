from django.shortcuts import render
# Create your views here.

from django.shortcuts import render
def home(request):
    return render(request, 'home.html')  # Plantilla para la página principal

def catalog(request):
    return render(request, 'catalog.html')

def contacts(request):
    return render(request, 'contacts.html')
