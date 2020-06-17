from rest_framework import serializers
from CasaSuggestApp.models import Campaign
from CasaSuggestApp.models import Message
from CasaSuggestApp.models import Customer


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id',
                  'tenantId',
                  'buId',
                  'casaCampaignId')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id',
                  'content'
                  )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',
                  'tenantId',
                  'buId',
                  'casaCustomerId')

