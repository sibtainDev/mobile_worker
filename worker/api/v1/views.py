from rest_framework.decorators import api_view
from rest_framework.response import Response
from worker.models import Unit, Visit, Worker
from .serializers import UnitSerializer, VisitSerializer, MakeVisitSerializer


@api_view(['GET'])
def get_units_by_worker(request):
    try:
        phone_number = request.GET.get('phone_number')
        worker = Worker.objects.filter(phone_number=phone_number).first()
        if not worker:
            return Response({'error': 'Worker not found'}, status=400)
        units = Unit.objects.filter(worker=worker)
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def make_visit(request):
    try:
        serializer = MakeVisitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data['phone_number']
            unit_obj = serializer.validated_data['unit_id']
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']

            worker = Worker.objects.filter(phone_number=phone_number).first()
            if not worker:
                return Response({'error': 'Worker not found'}, status=400)

            if unit_obj.worker != worker:
                return Response({'error': 'Unit not found or not linked to worker'}, status=400)

            visit = Visit.objects.create(unit=unit_obj, latitude=latitude, longitude=longitude)
            serializer = VisitSerializer(visit)
            return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
