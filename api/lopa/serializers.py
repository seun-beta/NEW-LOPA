from django.db import models
from rest_framework import serializers

from .models import Cause

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = "__all__"
