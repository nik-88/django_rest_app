from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from districts.serializers import *


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def district_list(request):
    if request.method == 'GET':
        districts = District.objects.all()
        campus_district = Campus.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        serializer2 = CampusSerializer(campus_district, many=True)

        for i in range(len(serializer.data)):
            a={}
            for k in range(len(serializer2.data)):
                if serializer.data[i]['id'] == serializer2.data[k]['DistrictId']:
                    a["campus"+str(k)]=dict(serializer2.data[k])
            serializer.data[i]['Campuses'] = a

        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DistrictSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def district_detail(request, pk):

    try:
        district = District.objects.get(pk=pk)
    except District.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DistrictSerializer(district)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DistrictSerializer(district, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        district.delete()
        return HttpResponse(status=204)

@csrf_exempt
def campus_list(request):
    if request.method == 'GET':
        campuses = Campus.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CampusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def campus_detail(request, pk):

    try:
        campus = Campus.objects.get(pk=pk)
    except Campus.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampusSerializer(campus)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CampusSerializer(campus, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        campus.delete()
        return HttpResponse(status=204)
