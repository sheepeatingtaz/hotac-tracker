from django.db import models

from campaign.models.user import Pilot
from hotac.models import Mission


class CampaignMission(models.Model):
    def __str__(self):
        return self.mission.name

    mission = models.ForeignKey(Mission)
    turn = models.IntegerField(default=0)


class CampaignMissionParticipant(models.Model):
    def __str__(self):
        return "{} - {}".format(self.mission, self.pilot)

    class Meta:
        unique_together = (
            'pilot',
            'mission'
        )

    pilot = models.ForeignKey(Pilot)
    mission = models.ForeignKey(CampaignMission)
