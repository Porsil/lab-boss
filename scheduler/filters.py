import django_filters
from django_filters import DateFilter
from .models import Workload
from .forms import DateInput


class WorkloadFilter(django_filters.FilterSet):

    test_date = DateFilter(field_name="test_date",
                           label="Test Date",
                           widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Workload
        fields = ('analyst', 'test')
        exclude = ['test_date',]


class AllWorkloadFilter(django_filters.FilterSet):

    test_date = DateFilter(field_name="test_date",
                           label="Test Date",
                           widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Workload
        fields = ('analyst', 'test', 'status')
        exclude = ['test_date',]
