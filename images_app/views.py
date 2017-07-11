from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'images_app/home.html')
def test(request):
    return render(request, 'images_app/test.html')
