from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FingerSerializer
from .models import FingersModel

class FingersView(APIView):
    def post(self, request):
        serializer = FingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Data saved successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Data validation failed",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class A(APIView):
    def get(self, request):
        return Response({
            "message": "Hello World"
        }, status=status.HTTP_200_OK)