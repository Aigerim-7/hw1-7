# Generated by Django 4.0.2 on 2022-02-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.PositiveIntegerField(choices=[(1, 'Bad'), (2, 'Nice'), (3, 'Good'), (4, 'Fine'), (5, 'Amazing')], max_length=5, null=True),
        ),
    ]
