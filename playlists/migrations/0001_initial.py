# Generated by Django 4.0.4 on 2022-05-19 04:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.library')),
            ],
        ),
    ]
