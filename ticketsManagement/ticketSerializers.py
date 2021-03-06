from rest_framework import serializers
from ticketsManagement.models import EtatTicket, Ticket

""" ticket state serializer """
class EtatTicketSerializer(serializers.Serializer) :
    idEtatTicket = serializers.IntegerField()
    intituleEtatTicket = serializers.CharField()
    
    """ returns new valid ticket state object to save in the database """
    def create(self, validated_data):
        newEtatTicket = EtatTicket(**validated_data)
        newEtatTicket.save()
        return EtatTicket(**validated_data)

    """ updates an existing ticket state by new valid data """
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
""" ticket serializer """
class TicketSerializer(serializers.Serializer):
    idTicket = serializers.IntegerField(read_only = True,)
    intituleTicket = serializers.CharField()
    descriptionTicket = serializers.CharField()
    dateLimitTicket = serializers.DateTimeField(allow_null=True) 
    donneesTicket = serializers.CharField(max_length=255,allow_null=True)
    remarquesTicket = serializers.CharField(allow_null=True) 
    assistante = serializers.CharField(max_length=255,allow_null=True)
    etatTicket = EtatTicketSerializer() 
    file = serializers.FileField(allow_empty_file=True,read_only = True)
    
    """ returns a new valid ticket object to save in the database"""
    def create(self, validated_data):
        etatTicket = validated_data.pop('etatTicket',None)
        ticket = Ticket(**validated_data)
        ticket.__dict__['etatTicket_id'] = etatTicket['idEtatTicket']
        ticket.save()
        print(ticket.idTicket)
        return ticket
    
    """ updates an existing ticket object with new valid data """
    def update(self,instance,validated_data):
        instance.donneesTicket = validated_data.get('donneesTicket',instance.donneesTicket)
        instance.remarquesTicket = validated_data.get('remarquesTicket',instance.remarquesTicket)
        instance.assistante = validated_data.get('assistante',instance.assistante)
        instance.__dict__['etatTicket_id'] = validated_data.pop('etatTicket')['idEtatTicket']
        instance.save()
        return instance


