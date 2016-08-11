from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import View

from campaign.forms.squadron import SquadronForm
from campaign.models.user import Squadron, SquadronMember


class SquadronView(View):
    template_name = 'squadron/add.html'
    context_object_name = 'squadron'
    model = Squadron
    form_class = SquadronForm

    def form_valid(self, form):
        # Add the current user to the squadron, making them an admin
        self.object = form.save()
        try:
            my_pilot = SquadronMember.objects.get(
                pilot_owner=self.request.user.pilotowner,
                squadron=self.object,
            )
        except ObjectDoesNotExist:
            my_pilot = SquadronMember(
                pilot_owner=self.request.user.pilotowner,
                squadron=self.object,
                admin=True,
            )
            my_pilot.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('squadron:detail', kwargs={'pk': self.object.pk})




class SquadronCreate(SquadronView, CreateView):
    pass


class SquadronUpdate(SquadronView, UpdateView):
    pass

class SquadronDetail(SquadronView, DetailView):
    template_name = 'squadron/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['squadron_admin'] = context['squadron'].squadronmember_set.filter(pilot_owner=self.request.user.pilotowner).count() > 0
        return context


