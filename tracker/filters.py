import django_filters
from django_filters import DateFilter
from .models import Batch
from .forms import DateInput


class BatchFilter(django_filters.FilterSet):

    booked_in = DateFilter(field_name="booked_in",
                           label="Booked in",
                           widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Batch
        fields = ('priority', 'batch', 'material',
                  'booked_in', 'status')
        exclude = ['booked_in',]
