# Generated by Django 3.0.5 on 2020-04-09 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_coronacases_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CoronaCases',
        ),
        migrations.RemoveField(
            model_name='coronavirus',
            name='active_cases',
        ),
        migrations.RemoveField(
            model_name='coronavirus',
            name='new_cases',
        ),
        migrations.RemoveField(
            model_name='coronavirus',
            name='new_deaths',
        ),
    ]
