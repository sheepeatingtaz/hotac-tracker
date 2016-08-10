from django.views.generic import CreateView

from campaign.forms.squadron import SquadronCreate
from campaign.models.user import Squadron, SquadronMember


class SquadronCreate(CreateView):
    template_name = 'squadron/add.html'
    model = Squadron
    form_class = SquadronCreate

    def form_valid(self, form):
        # Add the current user to the squadron, making them an admin
        self.object = form.save()
        my_pilot = SquadronMember(
            pilot_owner=self.request.user.pilotowner,
            squadron=self.object,
        )
        return super().form_valid(form)