from django.db import models
from rest_framework import serializers

from .models import Cause, CauseBarrier, Consequence, ConsequenceBarrier, Event


class CauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cause
        fields = "__all__"


class CauseBarrierSerializer(serializers.ModelSerializer):

    class Meta:
        model = CauseBarrier
        fields = "__all__"


class ConsequenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consequence
        fields = "__all__"


class ConsequenceBarrierSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsequenceBarrier
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
