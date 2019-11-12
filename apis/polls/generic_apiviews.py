from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from apis.polls.models import Poll, Choice
from apis.polls.serializers import PollSerializer, ChoiceSerializer,\
         VoteSerializer

class PollListAPIView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceListAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

class CreateVoteAPIView(generics.CreateAPIView):
    serializer_class =  VoteSerializer
