from rest_framework import serializers

from reports.models import DailyReportsModel

class ReportsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReportsModel
        fields = DailyReportsModel.get_fields()