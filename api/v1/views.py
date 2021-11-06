from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.v1.serializers import UserSerializer, PollSerializer, QuestionSerializer, AnswerSerializer, ChoiceSerializer

from polls.models import Poll, Question, Answer, Choice
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class LatestPollsList(APIView):
    def get(self, request, format=None):
        polls = Poll.objects.all()[0:4]
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class PollDetail(APIView):
    def get_object(self, pk):
        try:
            return Poll.objects.filter(id=pk).get()
        except Poll.DoesNotExist:
            raise Http404

    def get(self, request, poll_id):
        poll = self.get_object(poll_id)

        serializer = PollSerializer(poll)
        return Response(serializer.data)



class PollViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Poll.objects.all()
        poll = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer, **kwargs):
        user = User.objects.get(id=1)
        print(self.request.data)
        serializer.save(user=user)