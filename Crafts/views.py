from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    #this should combine the html doc and later built data models to display the data with our chosen design
    return render(request, 'Crafts/index.html')