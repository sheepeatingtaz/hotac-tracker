from django.db import models

from campaign.models.empire import ImperialShip

AI = (
    ('S', 'Strike'),
    ('A', 'Attack'),
    ('X', 'Special'),
    ('F', 'Flee'),
)


class MissionArc(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)


class Mission(models.Model):
    def __str__(self):
        return self.name

    arc = models.ForeignKey(MissionArc)
    name = models.CharField(max_length=30)
    # map =
    # brief =


class EnemySquadron(models.Model):
    class Meta:
        unique_together = (
            'squadron_name',
            'mission'
        )

    def __str__(self):
        return "{} - {}".format(
            self.mission,
            self.squadron_name,
        )

    mission = models.ForeignKey(Mission)
    squadron_name = models.CharField(max_length=10)
    vector = models.CharField(max_length=6)
    arrival = models.IntegerField(default=0)
    ai = models.CharField(max_length=1, choices=AI, verbose_name="AI")


class EnemySquadronComposition(models.Model):
    class Meta:
        unique_together = (
            'enemy_squadron',
            'players'
        )

    def __str__(self):
        return "{} - {} - [{}p]".format(
            self.enemy_squadron.mission,
            self.enemy_squadron,
            self.players
        )

    enemy_squadron = models.ForeignKey(EnemySquadron)
    players = models.IntegerField()
    ship_type = models.ForeignKey(ImperialShip, blank=True, null=True)
    conditional_ps = models.IntegerField(null=True, blank=True)
    elite = models.BooleanField(default=False)
