# Generated by Django 2.0.5 on 2018-05-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('isbn', models.CharField(max_length=150, null=True)),
                ('print_year', models.SmallIntegerField(null=True)),
                ('read_already', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
