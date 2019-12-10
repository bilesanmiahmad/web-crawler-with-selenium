from rest_framework.serializers import ModelSerializer
from crawler.models import Schedule


class ScheduleSerializer(ModelSerializer):

    class Meta:
        model = Schedule
        fields = [
            'id', 'booking_number', 'loading_port', 
            'vessel_departure', 'vessel_name', 'discharge_port', 
            'created_by']