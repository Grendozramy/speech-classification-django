from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'workplace_user_network/index.html')
