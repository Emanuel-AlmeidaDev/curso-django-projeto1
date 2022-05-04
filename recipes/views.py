from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('HOME')


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return HttpResponse('CONTATO')