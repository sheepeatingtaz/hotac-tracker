from rest_framework.generics import UpdateAPIView

from campaign.models.campaign import CampaignMission
from campaign.serializers.campaign import MissionSerializer


class UpdateMission(UpdateAPIView):
    serializer_class = MissionSerializer
    queryset = CampaignMission.objects.all()
