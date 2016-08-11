from django.contrib.auth.models import User
from django.db import models


class PilotOwner(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User)
    # todo avatar


class Pilot(models.Model):
    class Meta:
        unique_together = (
            # 'campaign',
            'callsign',
        )

    def __str__(self):
        return "{} ({})".format(self.callsign, self.owner)

    # campaign = models.ForeignKey(Campaign)
    owner = models.ForeignKey(PilotOwner)
    pilot_skill = models.IntegerField(default=2)
    callsign = models.CharField(max_length=30)


class Squadron(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50, unique=True)
    invite_only = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)


class SquadronMember(models.Model):
    class Meta:
        unique_together = (
            'squadron',
            'pilot_owner',
        )

    squadron = models.ForeignKey(Squadron)
    pilot_owner = models.ForeignKey(PilotOwner)
    admin = models.BooleanField(default=False)


