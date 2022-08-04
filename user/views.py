from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)
    def post(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)
    def put(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)
    def delete(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)