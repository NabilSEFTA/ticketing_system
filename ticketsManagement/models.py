from datetime import date
from pyexpat import model
from django.db import models

""" ticket state model """
class EtatTicket(models.Model):
    idEtatTicket = models.IntegerField(primary_key=True)
    intituleEtatTicket = models.CharField(max_length=255)
    
""" ticket model """
class Ticket(models.Model) :
    idTicket = models.AutoField(primary_key=True)
    intituleTicket = models.CharField(max_length=255,null=False)
    descriptionTicket = models.TextField()
    dateLimitTicket = models.DateTimeField()
    donneesTicket = models.CharField(max_length=255,null=True)
    remarquesTicket = models.TextField(null=True)
    assistante = models.CharField(max_length=255,null=True)
    etatTicket = models.ForeignKey(EtatTicket,on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='tickets/',null=True)

    """ def __init__(self,intituleTicket,descriptionTicket,dateLimitTicket):
        self.intituleTicket = intituleTicket
        self.descriptionTicket = descriptionTicket
        self.dateLimitTicket = dateLimitTicket """
       
        
