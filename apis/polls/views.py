from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from apis.polls.models import Poll

def polls_list(request):
    print(request)
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    print('-------------------------')
    print(dir(polls))
    print('-------------------------')
    print(polls.values)
    print('-------------------------')
    print(polls.values())
    print('-------------------------')
    print(polls.values('question'))
    print('-------------------------')
    print(polls.values_list())
    print('-------------------------')
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    print(data)
    return JsonResponse(data)

def polls_detail(request):
    pass
