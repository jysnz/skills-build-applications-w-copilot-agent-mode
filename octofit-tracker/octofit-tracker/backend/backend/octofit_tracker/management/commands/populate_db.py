from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='testpass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='testpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='testpass')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3)

        # Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-06-01')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-06-02')
        Activity.objects.create(user=user3, activity_type='Swimming', duration=60, date='2025-06-03')

        # Leaderboard
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=80)
        Leaderboard.objects.create(user=user3, score=120)

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio workout for mornings', difficulty='Easy')
        Workout.objects.create(name='Strength Training', description='Full body strength training', difficulty='Medium')
        Workout.objects.create(name='HIIT', description='High intensity interval training', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
