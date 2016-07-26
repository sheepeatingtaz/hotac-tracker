from rest_framework.generics import CreateAPIView

from campaign.serializers.experience import KillSerializer


class ChalkKill(CreateAPIView):
    serializer_class = KillSerializer
