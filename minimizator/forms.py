from django.forms import ModelForm

from minimizator.models import Link


class MinimizerForm(ModelForm):
    class Meta:
        model = Link
        fields = ['main_link', ]
