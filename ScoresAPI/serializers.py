from rest_framework import serializers
from ScoresAPI.models import ScoreModel, StudentModel

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = ['marks']

class StudentSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(read_only=True, many=True)
    class Meta: 
        model = StudentModel
        fields = ['student_id', 'name', 'scores']

class NameIDSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')
    value = serializers.IntegerField(source='student_id')
    class Meta:
        model = StudentModel
        fields = ['label', 'value']