# Create your views here.

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from CasaSuggestApp.serializers import CampaignSerializer


@api_view(['POST'])
def campaigns(request):
    campaign_data = JSONParser().parse(request)
    campaign_serializer = CampaignSerializer(data=campaign_data)
    if campaign_serializer.is_valid():
        campaign_serializer.save()
        return JsonResponse(campaign_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(campaign_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def handle_messages():
    return None


def tutorial_list_published():
    return None
