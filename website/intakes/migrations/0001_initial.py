# Generated by Django 4.1.2 on 2022-10-07 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('prot_fac', models.PositiveIntegerField(default=0)),
                ('carb_fac', models.PositiveIntegerField(default=0)),
                ('fat_fac', models.PositiveIntegerField(default=0)),
                ('cal_fac', models.PositiveIntegerField(default=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time', models.DateField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intakes.food')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intakes.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]