from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    possible_printers = Printer.objects.filter(working == True)[:]
    output = ', '.join([q.printer_name for q in possible_printers])
    return HttpResponse(output)
