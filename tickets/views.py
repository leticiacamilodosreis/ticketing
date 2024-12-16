from django.http import HttpResponse
from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        novo_ticket = Ticket(submitter=username, body=body)
        novo_ticket.save()
        #return HttpResponse("Página de submissão funcionando. Ticket criado!")
        context= {'message': f'Ticket criado com sucesso, {username}!'}
        return render(request, 'submit.html', context)
    return render(request, 'submit.html')

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets':all_tickets})