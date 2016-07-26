from rest_framework import serializers

from campaign.models.empire import ImperialShip
from campaign.models.experience import Kill


class ImperialShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImperialShip
        fields = (
            'name',
            'tie',
            'large'
        )

