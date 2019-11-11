from django.urls import path

from apis.polls import views

urlpatterns = [
    path("polls/",views.polls_list, name="polls_list"),
    path("polls/<int:id>/",views.polls_detail, name="polls_detail"),
]
