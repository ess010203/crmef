from rest_framework import serializers
from .models import Answer ,Question ,Quiz




class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True, read_only=True)
	questions_count = serializers.SerializerMethodField()
	class Meta:
		model = Quiz
		fields = "__all__"
		read_only_fields = ["questions_count"]

	def get_questions_count(self, obj):
		return obj.question_set.all().count()





class QuestionSerializer(serializers.ModelSerializer):
	answer_set = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = "__all__"