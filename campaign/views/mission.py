from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from campaign.models.campaign import CampaignMission, CampaignMissionParticipant


class MissionPlayer(TemplateView):
    template_name = 'mission/player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mission'] = get_object_or_404(CampaignMission, pk=self.kwargs.get('mission_id'))
        context['pilot'] = get_object_or_404(CampaignMissionParticipant, pk=self.kwargs.get('pilot_id'))
        context['actions'] = [
            {'name': 'damage', 'colour': 'warning'},
            {'name': 'kills', 'colour': 'danger'},
        ]
        return context