from rest_framework import serializers

from campaign.models.campaign import CampaignMission


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignMission
        fields = (
            'turn',
        )