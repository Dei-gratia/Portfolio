# Generated by Django 4.0.2 on 2022-06-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_home_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='future_scope',
            field=models.TextField(blank=True),
        ),
    ]
