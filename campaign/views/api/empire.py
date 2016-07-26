from rest_framework.generics import ListAPIView

from campaign.models.empire import ImperialShip
from campaign.serializers.empire import ImperialShipSerializer

class Imps(ListAPIView):
    serializer_class = ImperialShipSerializer
    queryset = ImperialShip.objects.all()