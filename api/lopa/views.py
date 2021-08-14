from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Cause
from .serializers import CauseSerializer
from lopa import serializers


class Data(APIView):

    def get(self, request):
        cause = Cause.objects.all()
        cause_data = CauseSerializer(cause)
        return Response(cause_data.data)
