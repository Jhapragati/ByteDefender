# Generated by Django 5.0.2 on 2024-02-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPRSS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
