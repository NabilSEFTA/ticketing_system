from django.urls import path
from ticketsManagement.views import getTickets,createTicket,updateTicket,createEtatTicket,getEtatTicket,deleteTickets

urlpatterns = [
    path(r'getTickets',getTickets),
    path(r'createTicket',createTicket),
    path(r'updateTicket',updateTicket),
    path(r'createEtatTicket',createEtatTicket),
    path(r'getEtatTicket',getEtatTicket),
    path(r'deleteAllTickets',deleteTickets)
    
]