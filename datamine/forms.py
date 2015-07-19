from django import forms
from .models import DataMine, DataMineUrl


class DataMineForm(forms.ModelForm):
    """ Model form which contains and evaluate
        `DataMine` fields.
    """
    class Meta:
        model = DataMine
        fields = ('title', 'mine_type', 'sites', 'notes')