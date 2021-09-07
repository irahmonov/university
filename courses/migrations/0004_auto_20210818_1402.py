# Generated by Django 3.2.6 on 2021-08-18 09:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='speciality',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 18, 14, 2, 12, 418659)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='specialities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='courses.speciality'),
        ),
    ]