# Generated by Django 3.1.3 on 2021-04-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainningDiary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise_type', models.TextField(max_length=1000)),
                ('name', models.TextField(max_length=1000)),
                ('intensity', models.TextField(max_length=1000)),
                ('burned_kcal', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'trainning_diary',
            },
        ),
    ]
