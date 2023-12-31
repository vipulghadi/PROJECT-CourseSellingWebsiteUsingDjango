# Generated by Django 4.2.5 on 2023-12-11 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUserProfile',
            fields=[
                ('i_am', models.CharField(default='', max_length=100)),
                ('student_id', models.UUIDField(default=uuid.UUID('abcbc167-170e-40e0-8103-0b2d8bb3d2cc'), primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('college_name', models.CharField(max_length=100)),
                ('linkedin_id', models.URLField()),
                ('github_id', models.URLField()),
                ('social_id', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseCreatorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_am', models.CharField(default='', max_length=100)),
                ('creator_id', models.UUIDField(default=uuid.UUID('ad4dd224-c0ec-4199-987b-0e3c07e7830f'))),
                ('full_name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('college_name', models.CharField(max_length=100)),
                ('linkedin_id', models.URLField()),
                ('github_id', models.URLField()),
                ('social_id', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
