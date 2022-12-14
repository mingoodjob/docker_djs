from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from user.serializers import UserSerializer
from user.serializers_jwt import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import User

class UserView(APIView):
    # 유저 조회
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)
    def delete(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)

class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class UserCheckView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response({"message": "로그인한 상태 입니다."}, status=status.HTTP_200_OK)