from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django import forms

from campaign.models.user import Squadron


class SquadronForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper()
        self.helper.form_id = 'add_squadron'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

        # You can dynamically adjust your layout
        self.helper.layout = Layout(
            Fieldset(
                'Create New Squadron',
                'name',
                'invite_only',
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('save', 'save')
            ),
        )

    class Meta:
        model = Squadron
        fields = (
            'name',
            'invite_only',
        )
