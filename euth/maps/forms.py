from django import forms
from django.utils.translation import ugettext as _

from adhocracy4.categories import forms as category_forms
from adhocracy4.maps import widgets

from . import models


class MapIdeaForm(category_forms.CategorizableFieldMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.settings = kwargs.pop('settings_instance')
        super().__init__(*args, **kwargs)
        self.fields['point'].widget = widgets.MapChoosePointWidget(
            polygon=self.settings.polygon)
        self.fields['point'].error_messages['required'] = _(
            'Please locate your proposal on the map.')

    def save(self, commit=True):
        instance = super().save(commit=False)
        category = self.cleaned_data['category']
        instance.category = category
        if commit:
            instance.save()
        return instance

    class Meta:
        model = models.MapIdea
        fields = ['name', 'description', 'image', 'point']
