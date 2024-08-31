from django import forms
from .models import ConstructionCost

class ConstructionCostForm(forms.ModelForm):
    class Meta:
        model = ConstructionCost
        fields = ['material_quality', 'design_complexity', 'cost']
