# Generated by Django 3.1.2 on 2020-10-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_remove_course_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]