from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Cause, CauseBarrier, Consequence, ConsequenceBarrier, Event

from .serializers import CauseSerializer, CauseBarrierSerializer, \
    EventSerializer, ConsequenceSerializer, ConsequenceBarrierSerializer 
from lopa import serializers


class CauseData(APIView):

    def get(self, request):
        cause = Cause.objects.all().values("description", "initial_frequency", "event_id", "target_frequency")
        cause_list = list(cause)
        data = cause_list 
        new_data = CauseSerializer(data, many=True)
        return Response(new_data.data)

class CauseBarrierData(APIView):
    
    def get(self, request):
        cause_barrier = CauseBarrier.objects.all().values("description", "pfd", "cause_id")
        cause_barrier_list = list(cause_barrier)
        data = cause_barrier_list 
        new_data = CauseBarrierSerializer(data, many=True)
        return Response(new_data.data)


class ConsequenceData(APIView):
    
    def get(self, request):
        consequence = Consequence.objects.all().values("description", "initial_frequency", "target_frequency")
        consequence_list = list(consequence)
        data = consequence_list 
        new_data = ConsequenceSerializer(data, many=True)
        return Response(new_data.data)


class ConsequenceBarrierData(APIView):
    
    def get(self, request):
        consequence_barrier = ConsequenceBarrier.objects.all().values("description", "pfd", "consequence_id")
        consequence_barrier_list = list(consequence_barrier)
        data = consequence_barrier_list 
        new_data = ConsequenceBarrierSerializer(data, many=True)
        return Response(new_data.data)

class EventData(APIView):
    
    def get(self, request):
        event = Event.objects.all().values("description", "cause_id", "consequence_id")
        event_list = list(event)
        data = event_list 
        new_data = EventSerializer(data, many=True)
        return Response(new_data.data)
