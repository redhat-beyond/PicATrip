from django.db import migrations, transaction
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('users', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        users_list = [
            User.objects.create_user(
                'Test-user-profile3', 'Test@gmail.com', 'password777'
            ),
            User.objects.create_user(
                'Test-user-profile4', 'Test2@gmail.com', 'password222'
            ),
        ]

        with transaction.atomic():
            for user in users_list:
                user.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
