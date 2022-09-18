from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from .models import Car
from django.http import JsonResponse
from .serializers import CarSerializer
from rest_framework import status


class ListCreateCarView(ListCreateAPIView):
    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(
                {'message': 'successful'},
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse({'message': 'failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    model = Car
    serializer_class = CarSerializer

    def put(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        serializer = CarSerializer(car, data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse({'message': 'Update successfully'},
                                status=status.HTTP_200_OK)
        return JsonResponse({'message': 'Update failed'},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        try:
            car.delete()
            return JsonResponse({'message': 'Delete successfully'},
                                status=status.HTTP_200_OK)
        except NameError:
            return JsonResponse({'message': f'Delete failed with {NameError}'},
                                status=status.HTTP_400_BAD_REQUEST)
