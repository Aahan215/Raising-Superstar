from django.db import models
from django.contrib.auth.models import User 

class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="activities")
    day_number = models.IntegerField()  # Represents Day 1, Day 2, etc.
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.program.name} - Day {self.day_number}"

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'activity')

    def __str__(self):
        return f"{self.user.username} - {self.activity.title} - {'Completed' if self.completed else 'Pending'}"
