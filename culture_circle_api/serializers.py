from rest_framework import serializers
from .models import Show


class ShowSerializers(serializers.ModelSerializers):
    class Meta:
        model = Show
        fields = ("id", "title", "region", "start_date", "end_date", "runtime", "min_price", "max_price")
