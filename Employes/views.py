from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Employer
from .serializers import EmployerSerializer

class EmployerViewSet(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)