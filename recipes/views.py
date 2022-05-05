from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'name': 'Emanuel Almeida'
    }
    return render(request, 'recipes/pages/home.html', context)
