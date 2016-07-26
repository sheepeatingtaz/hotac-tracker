from django.db.models.signals import post_save
from django.dispatch import receiver

from hotac.models import EnemySquadron, EnemySquadronComposition


@receiver(post_save, sender=EnemySquadron)
def create_empty_squadron(sender, instance, created, **kwargs):
    if created:
        for i in range(6):
            players = EnemySquadronComposition(
                enemy_squadron=instance,
                players=i+1
            )
            players.save()

