from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegistroSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def registro(request):
    serializer = RegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'mensagem': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)