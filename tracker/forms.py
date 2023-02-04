from django import forms


class DateInput(forms.DateInput):
    """
    defines the input type for calendar picker
    """
    input_type = 'date'
