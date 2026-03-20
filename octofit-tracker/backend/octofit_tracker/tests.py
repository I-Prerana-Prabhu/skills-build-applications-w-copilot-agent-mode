from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.username, 'testuser')

    def test_activity_creation(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        activity = Activity.objects.create(user=user, type='Run', duration=30, calories=300)
        self.assertEqual(str(activity), 'testuser2 - Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=20)
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(str(leaderboard), 'testuser3 - 100')
