from django.contrib import admin

from campaign.models.campaign import CampaignMission, CampaignMissionParticipant
from campaign.models.empire import ImperialShip
from campaign.models.user import PilotOwner, Pilot, Squadron


@admin.register(ImperialShip)
class StuffAdmin(admin.ModelAdmin):
    pass


@admin.register(CampaignMission, CampaignMissionParticipant)
class CampaignMissionAdmin(admin.ModelAdmin):
    pass

@admin.register(PilotOwner, Pilot)
class PilotAdmin(admin.ModelAdmin):
    pass

@admin.register(Squadron)
class SquadronAdmin(admin.ModelAdmin):
    pass