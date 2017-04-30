import django_tables2 as tables
from .models import user_data

class cat_table(tables.Table):
    class Meta:
        model=user_data
        attrs={'class':'paleblue'}
