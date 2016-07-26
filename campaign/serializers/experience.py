from rest_framework import serializers
from campaign.models.experience import Kill, Damage, KillAssist, GuardianAssist
from campaign.serializers.empire import ImperialShipSerializer


class KillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kill
        fields = (
            'pilotmission',
            'ship_type',
            'elite'
        )

    # ship_type = ImperialShipSerializer(many=True)
    def create(self, validated_data):
        return Kill.objects.create(**validated_data)

