# Generated by Django 2.2.2 on 2019-07-01 16:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=25)),
                ('lastname', models.CharField(default='', max_length=25)),
                ('username', models.CharField(default='', max_length=25, unique=True)),
                ('password', models.CharField(default='', max_length=25)),
                ('email', models.URLField(default='')),
                ('bitsid', models.CharField(max_length=20, unique=True)),
                ('contact', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(9999999999)])),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', editable=False, max_length=256)),
                ('marks', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_response', models.TextField(blank=True, max_length=2000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_portal.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_portal.Candidate')),
            ],
        ),
    ]
