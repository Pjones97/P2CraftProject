from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    #this should combine the html doc and later built data models to display the data with our chosen design
    # print("To the console!")
    # print(request)
    # return HttpResponse("Hello, world. You're at the index.") # This works!
    return render(request, "Crafts/index.html") # This line gives an error when you click Go To -> Implementations

def test(request):
    return render(request, "Crafts/test.html")