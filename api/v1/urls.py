from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AnswerViewSet, LatestPollsList, PollDetail

router_v1 = DefaultRouter(trailing_slash=True)

#router_v1.register(r'polls', PollViewSet, basename='poll', )
router_v1.register(r'answers', AnswerViewSet, basename='answer', )


urlpatterns = [
    path('latest-polls/', LatestPollsList.as_view()),
    path('polls/<slug:poll_id>/', PollDetail.as_view()),
]

urlpatterns += router_v1.urls