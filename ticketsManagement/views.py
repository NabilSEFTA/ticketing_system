from datetime import date, datetime
import io
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from ticketsManagement.models import EtatTicket, Ticket
from datetime import datetime
from ticketsManagement.ticketSerializers import TicketSerializer,EtatTicketSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Q
import json

""" returns set of tickets filtered or not, depending on request parameters """
def getTickets(request) :
    print()
    if(request.GET and request.GET['view']) :
        tickets = Ticket.objects.filter(Q(assistante  = request.GET['view'])|Q(assistante  = None))
    else :
        tickets = Ticket.objects.all()
    response = TicketSerializer(tickets,many=True).data
    return JsonResponse(response,safe=False)

""" returns a new ticket object or, an error when there are missing information """
@csrf_exempt
def createTicket(request) :
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    
    newTicket = TicketSerializer(data = data)
    if (newTicket.is_valid() ) :
        newTicket = newTicket.save()
        print(newTicket.idTicket)
        serializedNewTicket = TicketSerializer(newTicket)
        return JsonResponse(serializedNewTicket.data)
    return JsonResponse({'status':'false','message':'data is not valid !'}, status=500) 

""" update an existing ticket object with new data """
@csrf_exempt
def updateTicket(request) :
    
    data = request.POST['ticket']
    data = json.loads(data)
    id = data['idTicket']
    ticketInstance = Ticket.objects.get(idTicket = id)
    ticketInstance.file = request.FILES['file'] if request.FILES else None
    ticketInstanceModified = TicketSerializer(ticketInstance,data = data)
    
    if (ticketInstanceModified.is_valid() ) :
        ticketInstanceModified = ticketInstanceModified.save()
        ticketInstanceModified = TicketSerializer(ticketInstanceModified)
        return JsonResponse(ticketInstanceModified.data)
    return JsonResponse({'status':'false','message':'data is not valid !'}, status=500) 

""" def deleteTickets(request) :
    Ticket.objects.all().delete()
    return JsonResponse({'message' : 'ok'}) """

""" returns a new ticket state object """
@csrf_exempt
def createEtatTicket(request) :
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    newEtatTicket = EtatTicketSerializer(data = data)
    if (newEtatTicket.is_valid() ) :
        newEtatTicket.save()
        return JsonResponse(newEtatTicket.validated_data)
    return JsonResponse({'status':'false','message':'data is not valid !'}, status=500) 


""" returns all ticket state objects """
def getEtatTicket(request):
    etatsTicket = EtatTicket.objects.all()
    print(etatsTicket )
    serializedEtatsTicket = EtatTicketSerializer(etatsTicket,many = True)
    
    return JsonResponse(serializedEtatsTicket.data,safe=False)

""" updates an existing ticket state with new data or, returns an error when there are missing information """
@csrf_exempt
def UpdateEtatTicket(request) :
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    EtatTicket = EtatTicketSerializer(data = data)
    if (EtatTicket.is_valid() ) :
        EtatTicket.save()
        return JsonResponse(EtatTicket.validated_data)
    return JsonResponse({'status':'false','message':'data is not valid !'}, status=500) 

