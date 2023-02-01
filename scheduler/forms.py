from .models import Workload, Analyst, Test
from django import forms


class AnalystChoices(forms.ModelForm):
    """ Gets a list of available analysts """
    analyst_choices = Analyst.objects.all().values_list('name', 'name')
    analyst_list = []
    for choice in analyst_choices:
        analyst_list.append(choice)


class TestChoices(forms.ModelForm):
    """
    Gets a list of available tests
    """
    test_choices = Test.objects.all().values_list('name', 'name')
    test_list = []
    for choice in test_choices:
        test_list.append(choice)


class DateInput(forms.DateInput):
    """
    defines the input type for calendar picker
    """
    input_type = 'date'


class WorkloadForm(forms.ModelForm):
    """
    edit workload card form
    """
    class Meta:
        model = Workload
        fields = ('test_date', 'analyst', 'test', 'comment')
        widgets = {
            'test_date': DateInput(attrs={'class': 'form-control'}),
            'analyst': forms.Select(choices=AnalystChoices.analyst_choices,
                                    attrs={'class': 'form-control'}),
            'test': forms.Select(choices=TestChoices.test_choices,
                                 attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }
