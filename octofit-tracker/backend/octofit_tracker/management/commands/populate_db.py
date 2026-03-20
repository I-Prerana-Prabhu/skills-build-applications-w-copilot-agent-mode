from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', first_name='Steve', last_name='Rogers')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent')

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='Run', duration=30, calories=300)
        app_models.Activity.objects.create(user=batman, type='Swim', duration=45, calories=400)
        app_models.Activity.objects.create(user=captain, type='Bike', duration=60, calories=500)
        app_models.Activity.objects.create(user=superman, type='Fly', duration=120, calories=1000)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=ironman, points=1000)
        app_models.Leaderboard.objects.create(user=batman, points=900)
        app_models.Leaderboard.objects.create(user=captain, points=950)
        app_models.Leaderboard.objects.create(user=superman, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
