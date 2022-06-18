from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Api.models import Belge
from Api.serializers import BelgeSerializer

def index(request):
    context = dict()
    return render(request, 'index.html', context)

@api_view(['GET', 'POST'])
def belge_list_create_api_view(request):
    if request.method == 'GET':
        belgeler = Belge.objects.all()
        """belgeler = Belge.objects.filter(aktif=True)"""
        serializer = BelgeSerializer(belgeler,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BelgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def belge_detail_api_view(request,pk):
    try:
        belge_instance = Belge.objects.get(pk=pk)
    except Belge.DoesNotExist:
        return Response(
            {
                'errors':{
                    'code': 404,
                    'messege': f"({pk}) numaralı kayıt bulunamadı !!"
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method=='GET':
        serializer = BelgeSerializer(belge_instance)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = BelgeSerializer(belge_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif  request.method=='DELETE':
        belge_instance.delete()
        return Response(
            {
                'silme_işlemi':{
                    'code': 204,
                    'messege': f"({pk}) numaralı kayıt silinmiştir."
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )