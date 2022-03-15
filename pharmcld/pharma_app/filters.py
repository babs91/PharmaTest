import django_filters
from django_filters import DateFilter

from .models import products, adminEntry, customer_orders


class itmFilters(django_filters.FilterSet):

    class Meta:
        model = products
        fields = '__all__'
        exclude = ['status','product_no']


class clnFilters(django_filters.FilterSet):

    start_date = DateFilter(field_name='dateCreated', lookup_expr='gte')
    end_date = DateFilter(field_name='dateCreated', lookup_expr='lte')
    class Meta:
        model = adminEntry
        fields = '__all__'
        exclude = ['Amount', 'customers_address', 'Quantity', 'Phone', 'dateCreated']

class odrFilters(django_filters.FilterSet):

    start_date = DateFilter(field_name='dateCreated', lookup_expr='gte')
    end_date = DateFilter(field_name='dateCreated', lookup_expr='lte')
    class Meta:
        model = customer_orders
        fields = '__all__'
        exclude = ['customer_name', 'product_name', 'Quantity', 'Amount', 'Email', 'customers_address']

