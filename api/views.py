from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework import viewsets
# Create your views here.


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    