# Generated by Django 4.2.5 on 2023-12-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_usercoursedetails_is_paid_delete_usercourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoursedetails',
            name='buy_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
