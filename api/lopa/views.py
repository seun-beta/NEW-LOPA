from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Cause, CauseBarrier, Consequence, ConsequenceBarrier, Event

from .serializers import CauseSerializer, CauseBarrierSerializer, \
    EventSerializer, ConsequenceSerializer, ConsequenceBarrierSerializer 
from lopa import serializers


class Data(APIView):

    def get(self, request):
        cause = Cause.objects.all().values("description", "initial_frequency", "event_id", "target_frequency")
        cause_barrier = CauseBarrier.objects.all().values("description", "pfd", "cause_id")
        consequence = Consequence.objects.all().values("description", "initial_frequency", "target_frequency")
        consequence_barrier = ConsequenceBarrier.objects.all().values("description", "pfd", "consequence_id")
        event = Event.objects.all().values("description", "cause_id", "consequence_id")

        cause_list = list(cause)
        cause_barrier_list = list(cause_barrier)
        consequence_list = list(consequence)
        consequence_barrier_list = list(consequence_barrier)
        event_list = list(event)
        
        combined = cause_list + cause_barrier_list + consequence_list + consequence_barrier_list + event_list
        print(combined)
        new_data = CauseSerializer(combined, many=True)
        return Response(new_data.data)
