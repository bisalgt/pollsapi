from django.urls import path

from apis.polls import views
from apis.polls import apiviews

urlpatterns = [
    path("polls/",views.polls_list, name="polls_list"),
    path("poll/<int:id>/",views.polls_detail, name="polls_detail"),
    path("polls_api/",apiviews.PollList.as_view(), name="polls_api_list"),
    path("poll_api/<int:id>/",apiviews.PollDetail.as_view(), name="poll_api_detail"),
]
