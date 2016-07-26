from django.db import models

from campaign.models.campaign import CampaignMissionParticipant
from campaign.models.empire import ImperialShip


class Xp(models.Model):
    pilotmission = models.ForeignKey(CampaignMissionParticipant)
    points = models.IntegerField(default=1)


class Kill(Xp):
    ship_type = models.ForeignKey(ImperialShip)
    elite = models.BooleanField(default=False)


class Damage(Xp):
    pass


class KillAssist(Xp):
    pass


class GuardianAssist(Xp):
    pass


class MissieonBonus(Xp):
    description = models.CharField(max_length=20)
