# Generated by Django 4.1.7 on 2023-03-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("ID_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.TextField(max_length=255)),
                ("idade", models.IntegerField()),
            ],
        ),
    ]