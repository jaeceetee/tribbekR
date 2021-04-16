from .models import Questions
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['game_id', 'question_num', 'question', 'answer', 'wrong1','wrong2','wrong3','truefalse']
    # question = serializers.CharField(max_length=500, allow_blanks=False)
    # game_id = serializers.IntegerField(max_value=None, min_value=None)
    # question_num = serializers.IntegerField(max_value=None, min_value=None)
    # answer = serializers.CharField(max_length=200)
    # wrong1 = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    # wrong2 = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    # wrong3 = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    # truefalse = serializers.BooleanField()