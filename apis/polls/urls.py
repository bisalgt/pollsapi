from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authview

from apis.polls import views
from apis.polls import apiviews
from apis.polls import generic_apiviews

router = DefaultRouter()
router.register('polls_router_view', generic_apiviews.PollViewSet, basename='polls')

urlpatterns = [
    path("polls/",views.polls_list, name="polls_list"),
    path("poll/<int:id>/",views.polls_detail, name="polls_detail"),
    path("polls_api/",apiviews.PollList.as_view(), name="polls_api_list"),
    path("poll_api/<int:pk>/",apiviews.PollDetail.as_view(), name="poll_api_detail"),
    path("polls_api/<int:pk>/choices/<int:choice_pk>/vote/",apiviews.CreateVoteAPIView.as_view(), name="vote_api"),
    path("polls_generic_api/",generic_apiviews.PollListAPIView.as_view(), name="polls_generic_api_list"),
    path("poll_generic_api/<int:pk>/",generic_apiviews.PollDetailAPIView.as_view(), name="poll_generic_api_detail"),
    path("polls_generic_api/<int:pk>/choices/", generic_apiviews.ChoiceListAPIView.as_view(), name="choices_generic_api_list"),
    path("polls_generic_api/<int:pk>/choices/<int:choice_pk>/vote/", generic_apiviews.CreateVoteAPIView.as_view(), name="votes_generic_api"),
    path("users/", generic_apiviews.UserCreateAPIView.as_view(), name="users"),
    path("login/", generic_apiviews.LoginView.as_view(), name="login"),
    path("login_rest/", authview.obtain_auth_token, name="login_rest"),
]

urlpatterns += router.urls