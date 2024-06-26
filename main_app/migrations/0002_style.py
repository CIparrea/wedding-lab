# Generated by Django 5.0.3 on 2024-04-04 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('style', models.CharField(choices=[('M', 'Modern'), ('T', 'Traditional'), ('R', 'Rustic')], default='M', max_length=1)),
                ('wedding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.wedding')),
            ],
        ),
    ]
