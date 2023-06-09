# Generated by Django 4.2.1 on 2023-06-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that full_name already      exists.'}, max_length=150, null=True, verbose_name='username'),
        ),
    ]
