from django.shortcuts import render
from django.http import JsonResponse
from .serializer import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


def unit(request):
    if request.method=='GET':
        try:
            if request.headers.get('phone'):
                phone = request.headers.get('phone')
                print(phone)
                if Worker.objects.get(phone_number=phone):
                    worker_object = Worker.objects.get(phone_number = phone)
                    unit_object = Unit.objects.get(worker=worker_object)
                    serialized_data = UnitSerializer(unit_object)
                    return JsonResponse(serialized_data.data)
                return JsonResponse({"message":"Phone no does not exist in database"}, status=404)
            return JsonResponse({"message":"Please provide phone no as 'phone' in header"}, status=404)
        except Exception as e:
            return JsonResponse ({"message":str(e)}, status=404)
    return JsonResponse({"message":"Please change the request method into the 'get' method "}, status=404)    

@csrf_exempt
def visit(request, pk=None):
    if request.method=='POST':
        try:
            if request.headers.get('phone'):
                phone = request.headers.get('phone')
                if Worker.objects.filter(phone_number = phone):
                    unit_object = Unit.objects.get(id=pk)
                    if unit_object.worker.phone_number == phone :
                        latitude = float(request.POST.get('latitude'))
                        longitude = float(request.POST.get('longitude'))
                        visit_object=Visit.objects.create(latitude=latitude,longitude=longitude,unit=unit_object)
                        visit_object.save()
                        serialized_data = VisitSerializer(visit_object)
                        return JsonResponse(serialized_data.data)
                    return JsonResponse({"message":"Phone no is not match with the id"}, status=404)
                return JsonResponse({"message":"Phone no does not exist in database"}, status=404)
            return JsonResponse({"message":"Please provide phone no as 'phone' in header"}, status=404)
        except Exception as e:
            return JsonResponse ({"message":str(e)}, status=404)
    return JsonResponse({"message":"Please change the request method into the 'post' method "}, status=404)
    


            
                    




                    











