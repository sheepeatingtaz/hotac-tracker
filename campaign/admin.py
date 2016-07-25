from django.contrib import admin

from campaign.models.empire import ImperialShip


@admin.register(ImperialShip)
class StuffAdmin(admin.ModelAdmin):
    pass
