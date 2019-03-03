from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from update.models import Printer

# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    possible_printers = Printer.objects.filter(working = True)[:]
    output = ', '.join([q.printer_name for q in possible_printers])
    return HttpResponse(output)


def status(request, printer_id):
    try:
        found_printer = Printer.objects.get(id = printer_id)
    except Printer.DoesNotExist:
        raise Http404("Printer Does Not Exist")
    return HttpResponse(found_printer.working)

def newUpdate(request, printer_id):
    this_printer = Printer.objects.get(id = printer_id)
    info = request.POST['choice']
    this_printer.working = info
    this_printer.save()
    return HttpResponseRedirect(reverse('<int:printer_id>/'))



# want to add proximity
