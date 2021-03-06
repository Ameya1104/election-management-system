# Generated by Django 3.1.2 on 2020-10-21 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_result', models.DateField()),
                ('vote_count', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Election.candidate')),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Election.election')),
            ],
        ),
    ]
