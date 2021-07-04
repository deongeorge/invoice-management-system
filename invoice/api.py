from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *



class InvoiceList(APIView):
    def get(self, request):
        model = Invoice.objects.all()
        serializer = InvoiceSerializer(model, many = True)
        return Response(serializer.data)
    def post(self, request):
        model = Invoice.objects.all()
        serializer = InvoiceSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)