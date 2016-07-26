from django.contrib import admin

from hotac.models import EnemySquadronComposition, EnemySquadron, Mission, MissionArc


@admin.register(MissionArc, Mission, EnemySquadron, EnemySquadronComposition)
class HotACAdmin(admin.ModelAdmin):
    pass
