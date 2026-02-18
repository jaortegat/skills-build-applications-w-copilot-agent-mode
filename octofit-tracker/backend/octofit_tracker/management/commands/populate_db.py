from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Equipos
        marvel = Team.objects.create(name='marvel', description='Equipo Marvel')
        dc = Team.objects.create(name='dc', description='Equipo DC')

        # Usuarios
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel'),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel'),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc'),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc'),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Iron Pushups', description='Pushups estilo Ironman', suggested_for='marvel'),
            Workout.objects.create(name='Bat Cardio', description='Cardio intenso estilo Batman', suggested_for='dc'),
        ]

        # Actividades
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], type='swim', duration=25, date=timezone.now())
        Activity.objects.create(user=users[3], type='yoga', duration=60, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=80)
        Leaderboard.objects.create(user=users[2], points=120)
        Leaderboard.objects.create(user=users[3], points=90)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de ejemplo.'))
