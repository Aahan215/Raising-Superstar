from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Program, Activity, UserActivity
from .serializers import ProgramSerializer, ActivitySerializer, UserActivitySerializer

# List all programs
class ProgramListView(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

# Get activities for a program (Day 14-21)
class ActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        program_id = self.kwargs.get('program_id')
        start_day = self.request.query_params.get('start_day', 14)
        end_day = self.request.query_params.get('end_day', 21)
        return Activity.objects.filter(program_id=program_id, day_number__range=(start_day, end_day))

# Mark an activity as complete
class MarkActivityCompleteView(generics.CreateAPIView):
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        activity_id = request.data.get("activity_id")
        activity = get_object_or_404(Activity, id=activity_id)
        
        user_activity, created = UserActivity.objects.get_or_create(user=user, activity=activity)
        user_activity.completed = True
        user_activity.save()

        return Response({"message": "Activity marked as complete"}, status=status.HTTP_200_OK)

# Get user progress
class UserProgressView(generics.RetrieveAPIView):
    def get(self, request, user_id, program_id):
        completed_activities = UserActivity.objects.filter(user_id=user_id, activity__program_id=program_id, completed=True).values_list('activity__day_number', flat=True)
        all_activities = Activity.objects.filter(program_id=program_id).values_list('day_number', flat=True)

        response = {
            "completed_days": list(completed_activities),
            "pending_days": list(set(all_activities) - set(completed_activities))
        }
        return Response(response)
