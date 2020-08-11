from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ScoresAPI.models import StudentModel, ScoreModel
from ScoresAPI.serializers import StudentSerializer, ScoreSerializer, NameIDSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

@api_view(["GET"])
@csrf_exempt
def get_students(request):
    student = StudentModel.objects.filter()
    serializer = NameIDSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
@csrf_exempt
def get_scores(request, id):
    student = StudentModel.objects.get(student_id=id)
    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
@csrf_exempt
def put_score(request):
    student_id = request.POST['student_id']
    name = request.POST['name']
    score = request.POST['score']
    try:
        StudentModel.objects.get_or_create(student_id=student_id, name=name)
    except:
        return Response({'What Happened?':'Axe Happened'},status=status.HTTP_404_NOT_FOUND)
        # The Response message is a joke instead of a normal error message. Take it as such.
    ScoreModel.objects.create(s_id_id=student_id,marks=score)
    return Response({'What Happened?':'Successfully Created'}, status=status.HTTP_201_CREATED)
