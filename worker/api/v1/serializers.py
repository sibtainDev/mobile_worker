from rest_framework import serializers

from worker.models import Unit, Visit, Worker


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class MakeVisitSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    unit_id = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    latitude = serializers.DecimalField(max_digits=10, decimal_places=8)
    longitude = serializers.DecimalField(max_digits=11, decimal_places=8)


class VisitSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Visit
        fields = ['id', 'datetime', 'worker', 'unit']