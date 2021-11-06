from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField, SlugRelatedField
from rest_framework.fields import CurrentUserDefault

from users.models import Profile

from polls.models import Poll, Question, Answer, Choice

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(
    many=False,
    read_only=True,
    slug_field='role'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'date_joined', 'role']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    poll = serializers.SlugRelatedField(
    many=False,
    read_only=True,
    slug_field='title'
    )

    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text', 'choices', 'choice_type', 'poll'] 



class PollSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'start_date', 'end_date', 'questions']


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.SlugRelatedField(
    slug_field='username', read_only=True)
    #question = serializers.SlugRelatedField(slug_field='id', read_only=True)
    #choices = ChoiceSerializer(many=True)
    
    
    class Meta:
        model = Answer
        fields = ['id', 'user', 'answer_text', 'created', 'choices', 'question']