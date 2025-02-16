from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import ProgramListView, ActivityListView, MarkActivityCompleteView, UserProgressView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('programs/', ProgramListView.as_view(), name='program-list'),
    path('programs/<int:program_id>/activities/', ActivityListView.as_view(), name='activity-list'),
    path('user-activities/', MarkActivityCompleteView.as_view(), name='mark-activity-complete'),
    path('user-activities/<int:user_id>/programs/<int:program_id>/', UserProgressView.as_view(), name='user-progress'),
]
